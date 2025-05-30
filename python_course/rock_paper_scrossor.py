import random

computer_choice = random.choice(['rock', 'paper', 'scrissors'])
user_choice = input('Do you want rock, paper, or scrissors?')

print('Computer choice:', computer_choice)

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scrissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'scrissors' and computer_choice == 'paper':
    print('WIN')
else:
    print('You lose, computer wins :)')