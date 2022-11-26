def p(userNumber = int()):
    from random import randint
    number = randint(0, 10)
    
    if userNumber >= 0 and userNumber <= 10:
        if userNumber == number:
            print('you won!'.title())
        elif userNumber != number:
            print("You've lost!".title())
        else:
            print('End')
    else:
        print('End')

a = int(input())
p(a)