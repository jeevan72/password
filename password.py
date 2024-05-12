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
     pet=input("enter your pet's name:")
     return(l+n+a+s+pet)
if i=='p':
      passw()
elif i=='s':
     with open("passwordir.txt", "r") as f:
        content = f.read()
        print(content)
else:
      print("invalid input")
      exit()