import os


def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    continue_calc = 'y'
    num_1 = float(input('Enter a number : '))
    num_2 = float(input('Enter another number : '))
    ans = num_1+num_2
    values_entered = 2
    print(f'Current result : {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n)'))
        while continue_calc not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n)'))

        if continue_calc == 'n':
            break
        else:
            num = float(input("Enter another number"))
            ans += num
            print(f'Current result : {ans}')
            values_entered += 1

    return [ans, values_entered]


def subtraction():
    os.system('cls' if os.name == "nt" else 'clear')
    print('subtraction')

    continue_calc = 'y'
    num_1 = float(input("Enter a number : "))
    num_2 = float(input("Enter another number : "))
    ans = num_1-num_2
    value_entered = 2
    print(f'Current result : {ans}')

    while continue_calc == 'y':
        continue_calc = (input("Enter more (y/n) : "))
        while continue_calc not in ['y', 'n']:
            print("Please enter \'y\' ir \'n\'")
            continue_calc = (input("Enter more (y/n) : "))
        if continue_calc.lower() == 'n':
            break
        else:
            num = float(input("Enter another number : "))
            ans -= num
            print(f'Current result : {ans}')
            value_entered += 1
    return [ans, value_entered]


def multiplication():
    os.system('cls' if os.name == "nt" else 'clear')
    print('Multiplication')

    continue_calc = 'y'
    num_1 = float(input("Enter a number : "))
    num_2 = float(input("Enter another number : "))
    ans = num_1*num_2
    value_entered = 2
    print(f'Current result : {ans}')
    while continue_calc == 'y':
        continue_calc = (input("Enter more (y/n) : "))
        while continue_calc not in ['y', 'n']:
            print("Please enter \'y\' ir \'n\'")
            continue_calc = (input("Enter more (y/n) : "))
        if continue_calc.lower() == 'n':
            break
        else:
            num = float(input("Enter another number : "))
            ans *= num
            print(f'Current result : {ans}')
            value_entered += 1
    return [ans, value_entered]


def division():
    os.system('cls' if os.name == "nt" else 'clear')
    print('Dicision')

    continue_calc = 'y'
    num_1 = float(input("Enter a number : "))
    num_2 = float(input("Enter another number : "))
    while num_2 == 0.0:
        print("Please enter a second number > 0")
        num_2 = float(input("Enter another number : "))
    ans = num_1/num_2
    value_entered = 2
    print(f'Current result : {ans}')
    while continue_calc == 'y':
        continue_calc = (input("Enter more (y/n) : "))
        while continue_calc not in ['y', 'n']:
            print("Please enter \'y\' ir \'n\'")
            continue_calc = (input("Enter more (y/n) : "))
        if continue_calc.lower() == 'n':
            break
        else:
            num = float(input("Enter another number : "))
            while num == 0.0:
                print("Please enter a number > 0")
                num = float(input("Enter another number : "))
            ans /= num
            print(f'Current result : {ans}')
            value_entered += 1
    return [ans, value_entered]


def calculator():
    quit = False
    while not quit:
        print("Simple calculator")
        print("Enter \'a\' for addition")
        print("Enter \'s\' for substraction")
        print("Enter \'m\' for multiplicaiton")
        print("Enter \'d\' for division")
        print("Enter \'q\' for quit")
        choise = input("Selection : ")
        match choise:
            case 'a':
                results = addition()
                print("Ans = ", results[0], 'total inputs : ', results[1])
            case 's':
                results = subtraction()
                print("Ans = ", results[0], 'total inputs : ', results[1])
            case 'm':
                results = multiplication()
                print("Ans = ", results[0], 'total inputs : ', results[1])
            case 'sd':
                results = division()
                print("Ans = ", results[0], 'total inputs : ', results[1])
            case 'q':
                quit = True
                continue
            case _:
                print("Sorry, invalid character")


if __name__ == '__main__':
    calculator()
