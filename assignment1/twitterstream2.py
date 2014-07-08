import json
import requests
from requests_oauthlib import OAuth1

api_key = "isBbAlpdcChIoYNdgoLpZGL5i"
api_secret = "ZPI7zakwVg0pG8FjJGm6M9GJ8x5vy36qRvDTkIzOCbexLhFQRe"
access_token_key = "25582334-E0luaFhyGoPbNGPUJUm4SzcMZl8QIUi8FTuYSmUJw"
access_token_secret = "EVfQv55gypyc8IvRTZymj96O1C1FsdtOhnDRvW2wUSpTy"

url = 'https://api.twitter.com/1.1/search/tweets.json?q=netduino'
url2 = 'https://stream.twitter.com/1/statuses/sample.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url2, auth=auth, stream=True)

for line in r.iter_lines():
  if line:
    print json.loads(line)
