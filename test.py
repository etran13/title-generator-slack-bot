from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
import json

url = "https://slack.com/api/chat.postMessage"

headers = {
    "Authorization": "Bearer xoxb-REDACTED",
    "Content-Type": "application/json; charset=utf-8"
}

data = json.dumps({
    "channel": "#ellies-wf-slackbot-test",
    "text": "Hello from PYTHON!"
}).encode("utf-8") #Encode data as a JSON object

request = Request(url, data, headers)

response = urlopen(request)
print(json.loads(response.read()))