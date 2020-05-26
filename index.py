import random

dice = [1, 2, 3, 4, 5, 6]

user = input('Enter (s) to start roll the dice: ')

while True:
    if user == 's':
        print(random.choice(dice))
        user = input('Play again or stop ? Enter (s) or (e): ')
    elif user == 'e':
        print('Thaks for playing!')
        break



