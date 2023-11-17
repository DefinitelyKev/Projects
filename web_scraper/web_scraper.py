import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.get("https://www.9news.com.au/new-south-wales")

results = {"text": [], "url": []}

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for element in soup.findAll(attrs={"class": "story__headline"}):
    headline = element.find("a")
    if headline is not None:
        text = headline.text.strip()
        link = headline.get("href")
        if (text, link) not in results:
            results["text"].append(text)
            results["url"].append(link)


df = pd.DataFrame({"Title": results["text"], "Url": results["url"]})
df.to_csv("names.csv", index=False, encoding="utf-8")
