import requests,re
res = requests.Session()

URL = "https://www.machine-liker.com/"

def checkLogin( cookie ):
    COOKIES = cookie
    try:
        RESP = res.get(
                URL,headers = {'cookie': COOKIES}
                )
        if ( "<strong>User ID:</strong>" in RESP.text ):
            return True
        else:
            return False
    except:
        return False
