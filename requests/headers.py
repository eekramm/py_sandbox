import requests

url = "https://icanhazdadjoke.com/"

# plain text returned
response = requests.get(url, headers={"Accept": "text/plain"})

# print(response.text)

# json returned
response2 = requests.get(url, headers={"Accept": "application/json"})
# print(response2.text)
# print(response2.json())

data = response2.json()
print(data["joke"])