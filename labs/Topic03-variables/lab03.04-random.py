# a program that prints out a random number between one and ten

import random

x=int(input("Enter a number at the bottom of a range: "))
y=int(input("Now, enter a number at the top of a range: "))

number = (random.randint(x,y))

print("Here {} is a random number between {} and {}".format(number, x, y))
