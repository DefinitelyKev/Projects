import requests
from bs4 import BeautifulSoup
import csv
import queue
import re
import time
import random
from threading import Thread, Lock
from requests.exceptions import RequestException

MAX_PRODUCTS = 20
chosen_url = "https://scrapeme.live/shop/"

urls = queue.PriorityQueue()
urls.put((1, chosen_url))

visited_urls = set()
products = queue.Queue()
lock = Lock()

session = requests.Session()


def queueWorker(
    urls: queue.PriorityQueue, products: queue.Queue, stop_flag: bool
) -> None:
    while not urls.empty() and not stop_flag:
        if products.qsize() >= MAX_PRODUCTS:
            stop_flag = True
            return
        _, current_url = urls.get()

        try:
            response = session.get(current_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
        except RequestException as e:
            print(f"Error fetching {current_url}: {e}")
            continue

        with lock:
            if current_url in visited_urls:
                continue
            visited_urls.add(current_url)

        crawlPage(soup, visited_urls, urls, chosen_url)
        scrapePage(soup, current_url, products)

        # time.sleep(random.randrange(1, 3))


def crawlPage(
    soup: BeautifulSoup, visited_urls: set, urls: queue.PriorityQueue, base_url: str
) -> None:
    for element in soup.select("a[href]"):
        url = element["href"]

        if base_url in url and url not in visited_urls:
            priority_score = (
                1 if re.match(r"^https://scrapeme\.live/shop/page/\d+/?$", url) else 0.5
            )
            urls.put((priority_score, url))


def scrapePage(soup: BeautifulSoup, current_url: str, products: queue.Queue) -> None:
    if products.qsize() >= MAX_PRODUCTS:
        return

    product_title_element = soup.select_one(".product_title")
    if product_title_element:
        name = product_title_element.text
        price = soup.select_one(".price").text if soup.select_one(".price") else "N/A"
        image = (
            soup.select_one(".wp-post-image")["src"]
            if soup.select_one(".wp-post-image")
            else "N/A"
        )

        print(f"Currently on {name} and price is {price}")
        product = {"name": name, "url": current_url, "price": price, "image": image}
        products.put(product)


def addToCSV(products):
    with open("products.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "url", "price", "image"])
        writer.writeheader()
        while not products.empty():
            writer.writerow(products.get())


stop_flag = False
num_workers = 4
threads = [
    Thread(target=queueWorker, args=(urls, products, stop_flag), daemon=True)
    for _ in range(num_workers)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

addToCSV(products)
