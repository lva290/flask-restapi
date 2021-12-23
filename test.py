import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 100, "name": "How to make REST APIs", "views": 1000},
    {"likes": 8, "name": "Zelda walkthrough", "views": 50},
    {"likes": 1000, "name": "Office setup", "views": 100000}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
response = requests.get(BASE + "video/2")
print(response.json())
