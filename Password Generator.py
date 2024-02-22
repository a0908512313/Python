import random
import string

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

length = input("Please enter the password length : ")
print('``Choose character set for password from these : \n1. Digits \n2. Letters \n3. Special characters \n4. Exit``')

character = ''

# Getting character set for the password
while (True):
    choise = int(input("Enter the number : "))
    if (choise == 1):
        # Adding letters to possible characters
        character += string.ascii_letters
    elif (choise == 2):
        character += string.digits
    elif (choise == 3):
        character += string.punctuation
    elif (choise == 4):
        break

password_list = []

for i in range(int(length)):
    randomchar = random.choice(character)
    password_list.append(randomchar)
    i += 1

password_string = ",".join(password_list)

print(f'Your password is : {password_string}')
