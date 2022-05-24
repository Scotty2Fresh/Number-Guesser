import numpy as np

def Main():
    MinValue = input('Input minimum Value: ')
    MaxValue = input ('Input Maximum Value: ')

    x = np.random.randint(MinValue, MaxValue)
    print(x)
    Guess(x, MinValue, MaxValue)


def Guess(x, MinValue, MaxValue):
    ans = input('Is {} your number? '.format(x))

    if ans == 'yes':
        print('Your number is {}!'.format(x))
    elif ans == 'no':
        HiLo = input('Is your number higher or lower? ')
        if HiLo == 'higher':
            NewMin = x
            x = np.random.randint(NewMin, MaxValue)
            Guess(x, NewMin, MaxValue)
        elif HiLo == 'lower':
            NewMax = x
            x = np.random.randint(MinValue, NewMax)
            Guess(x, MinValue, NewMax)
        else:
            print('Invalid Input!')
            Guess(x, MinValue, MaxValue)

Main()