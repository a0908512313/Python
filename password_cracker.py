number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

password = input('Please enter the password : ')
ArrayPassword = password.split()

cracked = []

for i in range(len(ArrayPassword)):
    for j in range(len(number)):
        if ArrayPassword[i] == number[j]:
            cracked[i] = number[j]

StrinCracked = ' '.join(cracked)

print('Your password is : ', StrinCracked)
