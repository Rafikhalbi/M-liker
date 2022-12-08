import requests
from re import search
res = requests.Session()
from bot.banner import banner

URL = "https://www.machine-liker.com/"

def validUser(cookie):
    banner()
    try:
        RESP = res.get(
                URL,headers = {"cookie": cookie}
                ).text
        NAME = search(
                r'<i class="fas fa-user"></i> (.*?)</a>',str(RESP)
                )[1]
        ID = search(
                r'<strong>User ID:</strong> (.*?)</h5>',str(RESP)
                )[1]
        print(
                f"\n\t(•) Active User: {NAME}\n\t(•) User ID: {ID}"
                )
    except expression as identifier:
        pass
    
