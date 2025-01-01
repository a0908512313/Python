import random

# region : init players' scores
player_number = int(input('Please enter the number of players : '))
scores = dict()
for i in range(player_number):
    scores[str(i+1)] = 0
# endregion


def get_true_num():  # get correct number function
    MIN = int(input('Please enter the smallest number : '))
    MAX = int(input('Please enter the biggest number : '))
    while True:
        if MIN < MAX:
            break
        else:
            print("The biggest number can not smaller than the smallest number")
    return random.randint(MIN, MAX)


def check(true, guess):  # check function
    if guess > true:
        print("Too big.")
    elif guess == true:
        print('Correct!!')
    else:
        print("Too small.")
