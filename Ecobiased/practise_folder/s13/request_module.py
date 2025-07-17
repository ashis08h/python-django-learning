import requests

response = requests.get("gttps://google.com")
print(response.text)