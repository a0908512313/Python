from random import *
password = input("Password: ")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
           "y", "0" "1", "2", "3", "4", "5", "5", "6", "7", "8", "9"]
guess = ""
while (guess != password):
    guess = ""
    for i in range(len(password)):
        guessletter = letters[randint(0, 35)]
        guess += str(guessletter)
    print(guess)
print("Your password is : ")
