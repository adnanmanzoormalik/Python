import requests
import requests

url = "https://api.example.com/users"

params = {
    "city": "Srinagar"
}

response = requests.get(url, params=params)
print(response)