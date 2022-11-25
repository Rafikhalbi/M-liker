import requests
import re
from bs4 import BeautifulSoup as parser
import json
rs = requests.Session()

class machineLiker:
    def __init__(self):
        self.url = 'https://www.machine-liker.com'

    def send_reaction(self,cookie,url):
        print(
                '\n(!) Jika Ingin Memilih Lebih Dari Satu gunakan Koma ex: 1,2,3\n[1] Like\n[2] Love\n[3] Care\n[4] Haha\n[7] Wow\n[8] Sad\n[16] Angry\n[A] All Reactions\n'
                )
        cursor = input(
                '(?) Masukan Pilihan: '
                )
        if(cursor in['a','A']):
            type_react = '1,2,3 4,7,8,16'
        else:
            type_react = cursor

        checkpost = rs.post(
                self.url+'/api/get-post-info/',headers={
                    'Host': 'www.machine-liker.com',
                    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
                    'accept': '*/*',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'x-requested-with': 'XMLHttpRequest',
                    'sec-ch-ua-mobile': '?1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
                    'sec-ch-ua-platform': '"Android"',
                    'origin': 'https://www.machine-liker.com',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.machine-liker.com/auto-reactions',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie':cookie
                    },data = {
                        'url':url
                        },allow_redirects=False
                ).json()
        if checkpost['status'] == 'ok':
            post_id = checkpost['post']['id']
            story = checkpost['post']['story']
        else:
            exit(
                    '(!) Post Not Found'
                    )
        xget = rs.get(
                self.url+'/send-reactions/?post_id={}&story={}'.format(post_id,story),headers={
                    'Host': 'www.machine-liker.com',
                    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://www.machine-liker.com/auto-reactions',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie':cookie
                    },allow_redirects=False
                )
        object_id = re.search(r'name="object_id" value="(.*?)"',str(xget.content))[1]
        referer = self.url+'/send-reactions/?post_id={}&story={}'.format(post_id,story)
        get_react = rs.post(
                self.url+'/api/send-reactions/',headers={
                    'Host': 'www.machine-liker.com',
                    'accept': '*/*',
                    'dnt': '1',
                    'x-requested-with': 'XMLHttpRequest',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.machine-liker.com',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': referer,
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie':cookie
                    },data = {
                        'object_id':object_id,
                        'reactions':type_react,
                        'limit':'50'
                        }
                ).json()
        print(get_react)
#        next_page = rs.get(
#                self.url+'/success/?type=queued',headers={
#                    'cookie':cookie
#                    }
#                )
#            print(next_page.content)

    def home(self,cookie,name,username):
        print(
                '''
                
 __   __         ___      ___   ___   _  _______  ______   
|  |_|  |       |   |    |   | |   | | ||       ||    _ |  
|       | ____  |   |    |   | |   |_| ||    ___||   | ||  
|       ||____| |   |    |   | |      _||   |___ |   |_||_ 
|       |       |   |___ |   | |     |_ |    ___||    __  |
| ||_|| |       |       ||   | |    _  ||   |___ |   |  | |
|_|   |_|       |_______||___| |___| |_||_______||___|  |_|

(•) User Active: {} | {}
                '''.format(name,username)
                )
        url_post = input(
                '(?) Url Post: '
                )
        self.send_reaction(cookie,url_post)

    def checkUser(self,cookie):
        user = rs.get(
                self.url,headers={
                    'cookie':cookie
                    }
                ).content
        try:
            name_user = re.search(r'<i class="fas fa-user"></i> (.*?)</a>',str(user))[1]
            user_id = re.search(r'<strong>User ID:</strong> (.*?)</h5>',str(user))[1]
        except:
            exit(
                    '(!) Your Cookies Invalid'
                    )
        self.home(cookie,name_user,user_id)

    def checkValid(self,cookie):
        check = parser(rs.get(
                self.url,headers={
                    'cookie':cookie
                    }
                ).content,'html.parser').find('title')
        print(check.text)
        if str(check.text) == 'Machine Liker - Facebook Auto Liker | Auto Reaction | Auto Followers & More':
            exit(
                    '(!) Your Cookies Invalid'
                    )
        elif str(check.text) == 'Dashboard - Machine Liker':
            return cookie
        else:
            pass
    def loginCookies(self):
        cookie = input(
                '(?) Machine-Liker Cookies: '
                )
        newCookie = self.checkValid(cookie)
        self.checkUser(newCookie)

if __name__ == '__main__':
    run = machineLiker()
    run.loginCookies()
