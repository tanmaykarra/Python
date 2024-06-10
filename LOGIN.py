#import starts
import curses
import os
import sys
from colorama import Fore, Back, Style 
# import emoji 
import smtplib, ssl
import random
import speedtest
import mysql.connector
#import ends

# #connection to the database
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="tanmay",
#   password="tanmaykarra"
# )


#clear starts
def clear():
  curses.setupterm()
  e3 = curses.tigetstr('E3') or b''
  clear_screen_seq = curses.tigetstr('clear') or b''
  os.write(sys.stdout.fileno(), e3 + clear_screen_seq)
#clear ends

#heading start
heading = "Hello! Welcome to HtGRAm WEBSITE!"
x = heading.title()
print(Fore.LIGHTWHITE_EX + Style.BRIGHT + x)
#heading end

print(Fore.RED+ "\n PICK ANY ONE FROM ABOVE:")

acc = {}

while True:
    print(Style.BRIGHT+ '')
    print(Fore.GREEN + '1. Register a New Account')
    print("2. Log in your Account")
    print("3. Delete an Account")
    print("4. Check your Internet Speed")
    print("5. Forgot passoword")

    ans = int(input(Fore.LIGHTWHITE_EX +"\n Enter your choice:"))
    clear()
    
#new account starts
    if (ans == 1):
        x = input(Fore.BLUE +"Enter your username:")
        if (acc.get(x)) == None:
            y = input("Enter your password:")
            acc[x]=y
        else:
            print(Fore.RED+ "ACCOUNT ALREADY REGISTERED")
            break
        more = input("\n Do you want to go on?(Yes/No)")
        if (more=='Yes'):
            print("\n Here you go")
        else:
            break
        clear()   
#new account end

#login start
    elif (ans == 2):
        u = input(Fore.CYAN + "Enter your username:")
        if (acc.get(u)) == None:
            print("ACCOUNT NOT REGISTERED")
            break
        else:    
            p = input("Enter the password:")
        def get_key(val):
            for key, value in acc.items():
                if val == value:
                    return key
        if (get_key(p))==None:
                print(Fore.RED + "\n Wrong Username or Password")
                break
        else:    
                print("\n Logged in")
                print(emoji.emojize(":grinning_face_with_big_eyes:"))  
        more_ = input("\n Do you want to go on?(Yes/No)")
        if (more_=='Yes'):
            print("\n Here you go")
        else:
            break
        clear()   
#login ends

#delete account starts
    elif (ans == 3):
        de = input(Fore.LIGHTMAGENTA_EX + "Enter your Username:")
        sure=input("\n Are you sure you want to delete your account?(Yes/No)")
        if sure=='Yes':
            acc.pop(de)
            print("Your account is deleted")
        else:
            print("your account is intact")
        _less = input(Fore.RED +"\n Do you want to go on?(Yes/No)")
        if (_less=='Yes'):
            print("\n Here we go")
        else:
            break  
        clear()     
#delete account ends

    #speedtest start
    elif (ans == 4):
        st = speedtest.Speedtest() 
        print("THIS IS YOUR INTERNET SPEED",st.download()) 
        more_less = input(Fore.RED +"\n Do you want to go on?(Yes/No)")
        if (more_less=='Yes'):
            print("\n Here we go")
        else:
            break  
        clear()
#speedtest ends

#otp starts
    elif (ans==5):
        receiver_email = input("Enter your email address:")
        s = smtplib.SMTP("smtp.gmail.com" , 587) 
        s.starttls()
        s.login("mailpython123q@gmail.com" , "vwbaijougcqvmyto")
        otp = random.randint(1000, 9999)
        otp = str(otp)
        s.sendmail("sender_email", receiver_email, otp)
        print("\n OTP sent succesfully...")
        check = input("\n Enter the OTP:")
        if (check==otp):
            find = input("Enter your  Username:")
            print(acc.get(find))
            if acc.get(find)==None:
                print (Fore.RED +"\n SORRY,NO ACCOUNT FOUND")
            
        else:
            print(Fore.RED +"\n Wrong otp")
        s.quit() 
        more_ = input(Fore.RED +"\n Do you want to go on?(Yes/No)")
        if (more_=='Yes'):
            print("\n Here we go")
        else:
            break  
#otp ends
    else:
        print(Fore.RED +"\n Invalid  option")
    clear()
#Invalid option ends
