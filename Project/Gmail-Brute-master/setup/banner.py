import os
import platform
from setup import colors
from setup.colors import r,g,y,c

logo = f"""
 ██████╗ ███╗   ███╗ █████╗ ██╗██╗        
██╔════╝ ████╗ ████║██╔══██╗██║██║        
██║  ███╗██╔████╔██║███████║██║██║        
██║   ██║██║╚██╔╝██║██╔══██║██║██║        
╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗   
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝   
                                          
██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
                             {c + "Author: "+y +"Hamza Zahid Taha Nauman Yesheb Mark"+r+"|"+g +"Info Security"}             
                                                                                                                   
"""
c = colors
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")

def banner():
    print(c.ran + logo)

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Github of Taha Nauman: https://github.com/mtahabn/COMP421-22-10279-Section-A  ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Github of Hamza Zahid: https://github.com/hamzahid98/Comp421-22-11157-A ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github of Yesheb Mark: https://github.com/yesheb100/Info-Security-Project ", "- " * 3+c.ran + "|\n")

def banner2():
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @yesheb ", "- " * 4 + c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
