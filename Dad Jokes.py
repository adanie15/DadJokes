import requests
from pyfiglet import figlet_format
from termcolor import colored
from colorama import init
from random import choice

init()

header = figlet_format("DAD JOKE 3000!")
header = colored(header, color="green")
print(header)

user_input = input("I want to tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url, 
                   headers={"Accept": "application/json"},
                   params={"term": user_input}
                   ).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}.")
    print(results[0]['joke'])
else:
    print(f"Sorry, there's no joke utilizing the term: {user_input}.")
