from random import*

Rock = '''   
    _______ 
---'   ____) 
      (_____)
      (_____)
      (____)
---.__(___)
'''


Paper = '''   
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''



Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


images = [Rock ,Paper, Scissors]
user = int(input())
if user >=3 or user <0:
    print('you Typed an Invalid number.You loose!')
else:
    print(f'{images[user]}')
    
    computer = randint(0,2)
    index = images[computer]
    print(f'Computer choose {index}')

    if user == 0 and computer == 1:
        print('You Loose')
    elif user == 1 and computer == 0:
        print('You Won')
    elif user == 0 and computer == 2:
        print('You Won')
    elif user == 2 and computer == 0:
        print('You Loose')
    elif user == 1 and computer == 2:
        print('You Loose')
    elif user == 2 and computer == 1:
        print('You Won')
    elif user == computer:
        print('You draw')






