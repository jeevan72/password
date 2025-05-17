import random as r
import pyperclip as pp
i=input("for:\nenter p for new password\nenter s for stored password").lower()
def passw():
        site=input("enter the site:") 
        n=input("enter need input custom or random password:")
        if n=="custom":
            char= custom()
        elif n=="random":
            char= "abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+ "
        else:
            print("invalid input")
            exit()      
        length=int(input("enter the length:"))
        passwor=""
        for a in range(length):
            passwor += r.choice(char)
        print("The password is ", passwor)
        pp.copy(passwor)
        con=site+" :"+passwor
        pa=open("passwordir.txt", "a")
        pa.write(con+"\n")
        pa.close()    
def custom():
     n=input("enter the name:")
     l=input("enter the lastname:")
     a=input("enter favorite color:")
     s=input("enter the symbols:")
     nu=input("enter the number:")
     pet=input("enter your pet's name:")
     return(l+n+a+s+pet+nu)
def check_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()_+" for c in password): score += 1
    return score
if i=='p':
      passw()
elif i=='s':
     with open("passwordir.txt", "r") as f:
        content = f.read()
        print(content)
else:
      print("invalid input")
      exit()