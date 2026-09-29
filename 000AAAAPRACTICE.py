#Q1 >>>. use this url >>> https://jsonplaceholder.typicode.com/posts
# Write a Python program that:
# 1. Imports requests.
# 2. Sends a GET request to the API.
# 3. Uses the query parameter userId=1.
# 4. Sets a timeout of 5 seconds.
# 5. Checks for HTTP errors using raise_for_status().
# 6. Converts the response to Python data using response.json().
# 7. Prints the total number of posts returned.
# 8. Prints the id and title of every returned post.
# 9. Handles Timeout, ConnectionError, and HTTPError using try/except.

import requests
try: 
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId" : 1}, timeout=5)
    response.raise_for_status()
    data = response.json()
    print(f"Total number of posts: {len(data)}")
    for user in data:
        print(user["id"], user["title"])
except requests.exceptions.ConnectTimeout as e:
    print("ERROR: ", e)
except requests.exceptions.ConnectionError as e:
    print("ERROR: ", e)
except requests.exceptions.HTTPError as e:
    print("ERROR: ", e)


#Q2 >>> url >>> https://jsonplaceholder.typicode.com/posts
# Write a Python program that:
# 1. Imports requests.
# 2. Creates this data: {
#     "title": "Learning Python APIs",
#     "body": "I am learning API requests with Python.",
#     "userId": 1
# }
# 3. Sends the data using a POST request with json=.
# 4. Sets a timeout of 5 seconds.
# 5. Checks for HTTP errors using raise_for_status().
# 6. Prints the status code.
# 7. Converts the response using response.json().
# 8. Prints the returned id, title, and userId.
# 9. Handles Timeout, ConnectionError, and HTTPError using try/except.

import requests
data = {
    "title": "Learning Python APIs",
    "body": "I am learning API requests with Python.",
    "userId": 1
}
try:
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data, timeout=5)
    response.raise_for_status()
    print("Status code: ", response.status_code)
    data = response.json()
    print(data["id"], data["title"], data["userId"])
except requests.exceptions.ConnectTimeout as e:
    print("ERROR: ", e)
except requests.exceptions.ConnectionError as e:
    print("ERROR: ", e)
except requests.exceptions.HTTPError as e:
    print("ERROR: ", e)