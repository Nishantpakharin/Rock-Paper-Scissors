import random

options = ['rock','paper','scissors']

ur_choice = input('choose rock, paper, scissors: ')
com_choice = random.choice(options)

print('You chose: ', ur_choice)
print('Computer chose: ', com_choice)

if ur_choice == com_choice:
    print('Its a draw!')

elif ur_choice == 'rock' and com_choice == 'scissors':
    print('You won!')

elif ur_choice == 'scissors' and com_choice == 'paper':
    print('You won!')

elif ur_choice == 'paper' and com_choice == 'rock':
    print('You won!')

else:
    print('computer wins!')        