import requests
import json
import jsonpath

#API Url
url = "https://reqres.in/api/users/?page=2"

# Send Get Request
response = requests.get(url)


# Parse response to Json format
json_response = json.loads(response.text)

print(json_response)

# Fetch value using Json Path, json path
total = jsonpath.jsonpath(json_response, "total")
print(total)


email = jsonpath.jsonpath(json_response, "data[0].email")
print(email)

