import random

numbers = '1234567890'
Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Upper = []
for i in range(len(Lower)):
    Upper[i] = Lower[i].upper()


all = Lower + Upper + numbers

length = input('Please input the length :')
