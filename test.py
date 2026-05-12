from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
import json

def getToken():
    file_path = "token.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()[0]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


url = "https://slack.com/api/chat.postMessage"

myToken = getToken()
headers = {
    "Authorization": myToken,
    "Content-Type": "application/json; charset=utf-8"
}

data = json.dumps({
    "channel": "#ellies-wf-slackbot-test",
    "text": "Hello from PYTHON!"
}).encode("utf-8") #Encode data as a JSON object

request = Request(url, data, headers)

response = urlopen(request)
print(json.loads(response.read()))