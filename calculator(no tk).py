import os


def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    continue_calc = 'y'
    num_1 = float(input('Enter a number : '))
    num_2 = float(input('Enter another number'))
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
