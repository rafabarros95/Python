import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit(print("Few Arguments passed"))


response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
# print(response.json())   print(response.json()["results"][0]["trackName"])
# print(json.dumps(response.json() , indent=4)) Ideendtation of the json response

data = response.json()
for song in data["results"]:
    print(song["trackName"])



