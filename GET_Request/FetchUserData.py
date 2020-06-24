import requests

#API Url
url = "https://reqres.in/api/users/?page=2"

# Send Get Request
response = requests.get(url)


# Display Response
print(response.content)


# Display response header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch Cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)


# if __name__ == '__main__':

