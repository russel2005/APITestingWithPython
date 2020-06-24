import requests

#API Url
url = "https://reqres.in/api/users/7"

# Send Get Request
response = requests.delete(url)


# get status code
print(response.status_code)

assert response.status_code == 204
