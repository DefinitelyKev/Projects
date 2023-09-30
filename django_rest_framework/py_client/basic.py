import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(
    endpoint, json={"title": "abc123", "content": "hello World", "price": "34"}
)
# print(get_response.headers)
print(get_response.json())
