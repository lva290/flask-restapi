import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/2", {"views":10000, "likes": 1001})
print(response.json())
