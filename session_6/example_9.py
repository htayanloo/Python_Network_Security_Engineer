import requests

response = requests.get("http://127.0.0.1:5000/")

print(response.json())

for item in response.json()["blacklist"]:
    print(item["ip"])