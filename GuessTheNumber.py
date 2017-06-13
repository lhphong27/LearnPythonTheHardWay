#Guess the number game
import random

a = random.randint(1, 20)
result = False

for i in range(5):
    guess_number = int(input('Type a number between 1 to 20: '))
    if(guess_number == a):
        result = True
        break
    elif(guess_number < a):
        print('Your number is less than correct number.')
    elif(guess_number > a):
        print('Your number is greater than correct number.')

if(result):
    print ('You win, The correct number is: ', a)
else:
    print ('You lose, The correct number is: ', a)