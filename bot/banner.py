from colorama import Fore,Back,Style,init
import os

def cls(osname):
    if ( osname == "posix" ):
        os.system("clear")
    else:
        os.system("cls")

init(True)

banner_home = f"""{Style.BRIGHT}

{Fore.BLUE}   _____            .____    .__ __{Fore.RESET}
  /     \           |    |   |__|  | __ ___________ 
{Fore.BLUE} /  \ /  \   ______ |    |   |  |  |/ // __ \_  __ \\{Fore.RESET}
/    Y    \ /_____/ |    |___|  |    <\  ___/|  | \/
{Fore.BLUE}\____|__  /         |_______ \__|__|_ \\\\___  >__|{Fore.RESET}
        \/                  \/       \/    \/       

"""

def banner():
    cls(os.name)
    print(
            banner_home,
            f"\t----- [ {Back.WHITE}{Fore.BLACK}MACHINE-LIKER{Fore.RESET}{Back.RESET} ] -----"
            )
