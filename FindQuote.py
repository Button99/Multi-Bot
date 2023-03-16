import requests
import json


def findQuote():
    try:
        res = requests.get("https://quoteapi.button99.repl.co/").json()
        msgRes = res["quote"] + "\n-" + res["name"]
        return msgRes
    except:
        return "Wait a lil bit :/"
