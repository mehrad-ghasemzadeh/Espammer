import requests 
from colorama import Fore,init
init()
import pyfiglet
import os 
os.system("cls" or "clear")

baner=pyfiglet.figlet_format("Web Spamer") 
print(Fore.LIGHTMAGENTA_EX+baner)      

url=input("Enter url : ") 

Spam_Text=input("Enter Comment : ")
Author_Text=input("Enter author : ") 
Email=input("Enter Email Fake : ")

Nos=int(input("Number of spam : "))
a=0
while a<=Nos: 

    pyload={
        "comment" : f"{Spam_Text}",
        "author" : f"{Author_Text}",
        "email" : f"{Email}",
        "submit" : "submit"
    }
    b=requests.post(url,pyload)
    a+=1
    print(Fore.GREEN+f"[ {Fore.MAGENTA+str(a)+Fore.GREEN} ]"+f"{Fore.BLUE+str(b)}")  
