import requests,json
from re import search
res = requests.Session()

URL = "https://www.machine-liker.com"

def start(posturl,cookie,type_react):
    CHECK = res.post(
            URL+"/api/get-post-info/",headers = {"cookie": cookie},data = {"url": posturl}
            ).json()
    if CHECK['status'] == 'ok':
            post_id = CHECK['post']['id']
            story = CHECK['post']['story']
    elif CHECK['status'] == 'fail':
        print("\r(!) Invalid Url / Spam From Server",)

    GETOI = res.get(
            URL+"/send-reactions/?post_id={}&story={}".format(post_id,story)
            ).text
    object_id = search(r'name="object_id" value="(.*?)"',str(GETOI))

    referer = URL+"/send-reactions/?post_id={}&story={}".format(post_id,story)
    RESPONSE = res.post(
            URL+"/api/send-reactions/",headers = {"referer": referer,"cookie": cookie},data = {"object_id": object_id,"reactions":type_react,"limit": "50"}
            ).json()
    print(RESPONSE)

def checkpost(posturl,cookie):
    print(
            '\n(!) Jika Ingin Memilih Lebih Dari Satu gunakan Koma ex: 1,2,3\n[1] Like\n[2] Love\n[3] Care\n[4] Haha\n[7] Wow\n[8] Sad\n[16] Angry\n[A] All Reactions\n'
            )
    CURSOR = input(
            "(?) Choose: "
            )
    if ( CURSOR == "a" or CURSOR == "A"):
        type_react = "1,2,3 4,7,8,16"
    else:
        type_react = CURSOR
    start(posturl,cookie,type_react)

