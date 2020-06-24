import requests

#API Url
url = "https://reqres.in/api/users/?page=2"

#Send Get Request
response = requests.get(url)

print(response.content)

# if __name__ == '__main__':

