import string
import random
base = list(string.ascii_letters)
target = 'helloworld'
temp = ['']*len(target)
for i in range(len(target)):
    while temp[i] != target[i]:
        temp[i] = random.choice(base)
        print("".join(temp))
