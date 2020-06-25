import requests
import json
import jsonpath

"""
Steps:
1. create payload
2. hit POST request
3. Parse response to json format
4.validate response
"""

#API Url
url = "https://reqres.in/api/users/469"

# REad input Json file
payload = {
    "name": "Russel updated",
    "job": "SDET updated"
}


def createUser(url, payload):
    """Send a notification using a Slack webhook URL. See https://api.slack.com/incoming-webhooks

    Arguments:
        url (string): Slack incoming webhook URL for sending the message.
        msg (string): The message to be sent (can use markdown for formatting)
    """
    try:

        # res = requests.post(url, data=json.dumps(payload))
        # or
        res = requests.put(url, json=payload)
        print("Status code: " + str(res))
        print("Response Header:")
        print(res.headers.get("Content-Type"))

        # Parse response to Json format
        json_response = json.loads(res.text)
        print(json_response)

        # pick id using JSON path
        name = jsonpath.jsonpath(json_response, "name")
        print(name)
        job = jsonpath.jsonpath(json_response, "job")
        print(job)

        if res.status_code != 200:
            print(f'Falied to send notification "{payload}" to "{url}"')
            print('Response', res.content)
            return False
    except Exception as e:
        print(f'Falied to send notification "{payload}" to "{url}"')
        print(e)
        return False
    return True


print(createUser(url, payload))
