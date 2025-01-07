import requests

url = "https://api.github.com/users/raimarsilva"

response = requests.get(url)

print("reposta: ", response.json())