from random import *
import os

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def crack():
    pw = ""
    u_pwd = input("Enter a password : ")
    while (pw != u_pwd):
        pw = ""
        for i in range(len(u_pwd)):
            guess_pwd = keys[randint(0, 34)]
            pw = str(guess_pwd) + str(pw)
    print(pw)
    print("Cracking Password...Please Wait")
    os.system("cls")
    print("Your Password Is : ", pw)

iscrack = True
crack()

while(iscrack == True):
    iscrack = input("If you want to continue enter 'Y' or enter 'N' : ")
    if(iscrack == "Y" or iscrack == "y"):
        crack()
    elif(iscrack == "N" or iscrack == "n"):
        iscrack = False
        print("bye~")
    else:
        continue