#Rolling the dice game

import random

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":

    print ("Rolling the dices...")
    print("The result is:")

    a = random.randint(min, max)
    b = random.randint(min, max)
    print "First dice:", a
    print 'Second dice:', b
    print 'You have', a+b, 'points'

    roll_again = raw_input("Do you want to try again? (Y/N) ")