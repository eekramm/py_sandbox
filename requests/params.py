import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": "fruit"}
)

# print(response.text)
# print(response.json())

data = response.json()
print(data)


