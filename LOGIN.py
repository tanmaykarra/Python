import curses
import os
import sys
from colorama import Fore, Back, Style 
import emoji 
import speedtest 
st = speedtest.Speedtest() 
print("THIS IS YOUR INTERNET SPEED",st.download())   
def clear():
  curses.setupterm()
  e3 = curses.tigetstr('E3') or b''
  clear_screen_seq = curses.tigetstr('clear') or b''
  os.write(sys.stdout.fileno(), e3 + clear_screen_seq)

acc = {}
while True:
    print(Style.BRIGHT+ '')
    print(Fore.GREEN + '1. Make a new account')
    print("2. Log in")
    print("3. Delete a account")

    ans = int(input(Fore.LIGHTWHITE_EX +"enter your choice:"))
    clear()
#new account starts
    if (ans == 1):
        x = input(Fore.BLUE +"enter a username:")
        if (acc.get(x)) == None:
            y = input("enter a password:")
            acc[x]=y
        else:
            print("you already have a account please login")
            break
        clear()   
#new account end
#login start
    elif (ans == 2):
        u = input(Fore.CYAN + "enter the username:")
        if (acc.get(u)) == None:
            print("your account was not found")
            break
        else:    
            p = input("enter the password:")
        def get_key(val):
            for key, value in acc.items():
                if val == value:
                    return key
        if (get_key(p))==None:
                print("wrong username or password")
                break
        else:    
                print("logged in")
                print(emoji.emojize(":grinning_face_with_big_eyes:"))  
        more = input("do you want to go on?(Yes/No)")
        if (more=='Yes'):
            print("here we go")
        else:
            break
        clear()   
#login ends
#delete account starts
    elif (ans == 3):
        de = input(Fore.LIGHTMAGENTA_EX + "enter your username:")
        sure=input("are you sure you want to delete your account?(Yes/No)")
        if sure=='Yes':
            acc.pop(de)
            print("Your account is deleted")
        else:
            print("your account is intact")
        clear()     
#delete account ends
#Invalid option            
    else:
        print(Fore.RED +"invalid  option")
    clear()     
#Invalid option ends
