import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": "sister"}
)

# print(response.text)
# print(response.json())

data = response.json()
print(data)


