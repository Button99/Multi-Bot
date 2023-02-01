import requests
import json

def findQuote():
  try:
    res = requests.get("https://api.quotable.io/random")
    jsonData = json.loads(res.text)
    msgRes = jsonData["content"] + "\n-" + jsonData["author"]
    return msgRes
  except:
    return "Wait a lil bit :/"    
