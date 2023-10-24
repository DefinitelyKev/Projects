import requests

endpoint = "http://127.0.0.1:8000/api/products/1/"

get_response = requests.get(
    endpoint, json={"title": "abc123", "content": "hello World", "price": "34"}
)
# print(get_response.headers)
print(get_response.json())
