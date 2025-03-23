# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# there can be draw also

print('====Rock,Paper,Scissors====')

print('Choose\n'
      'R for Rock\n'
      'P for Paper\n'
      'S for Scissors')

com = 'R'
you = input('Enter your choice: ')

if you == 'R' and com == 'R':
    print('Its a draw!')
elif you == 'P' and com == 'R':
    print('Won!, paper beats rock')
elif you == 'S' and com == 'R':
    print('lost!, rock beats scisssors')    