import string
import random
import time
base = list(string.ascii_letters)
base.append(" ")
target = input('Enter the text : ')
temp = ['']*len(target)
for i in range(len(target)):
    j = 1
    TIME = random.randint(20, 50)
    while temp[i] != target[i]:
        if j == TIME:
            temp[i] = target[i]
            break
        temp[i] = random.choice(base)
        print("".join(temp))
        time.sleep(0.05)
        j += 1
