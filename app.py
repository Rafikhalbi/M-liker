from utilities.login import checkLogin as CLOG
from utilities.checkActiveUser import validUser as valid
from bot.banner import banner
from utilities.checkPost import checkpost
import os

def checkAvailableFiles(file):
    try:
        with open(file) as CONFIG:
            COOKIE = CONFIG.read().replace("\n","")
            if ( CONFIG == "" ): exit(
                    ERRFILE
                    )
            else:
                return COOKIE
    except FileNotFoundError:
        exit(
                ERRFILE
    
                )

def remove(e):
    try:
        os.system(
                f"rm -rf {e}"
                )
    except:
        pass

def login(file):
    try:
        print(
              "\n(*) Check Cookies Login..."
              )
        if ( CLOG(file) ):
            print(
                    "(✓) Cookies Valid"
                    )
            valid(file)
            home(file)
        else:
            remove("config.txt")
            exit( ERRFILE )
    except:
        pass

def home(cookie):
    POSTURL = input(
            "\n(?) Post Url: "
            )
    checkpost(POSTURL,cookie)

if __name__ == "__main__":
    ERRFILE = "(!) Please Setup Your Machine Liker Cookies !"
    login(checkAvailableFiles("./config.txt"))
