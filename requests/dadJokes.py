import requests
import random

url = "https://icanhazdadjoke.com/search"
foundAJoke = False

while foundAJoke == False:

    print("What would you like to hear a joke about?")
    term = input()

    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": term}
    )

    results = response.json()["results"]
    # print(results)

    if len(results) == 0:
        print("Sorry I don't know any jokes about that :(")
    elif len(results) == 1:
        print(results[0]["joke"])
        foundAJoke = True
    elif len(results) > 1:
        joke = random.choice(results)
        print(joke["joke"])
        foundAJoke = True

