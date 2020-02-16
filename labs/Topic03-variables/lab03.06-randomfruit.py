# this programme types out random fruit

import random

fruits = ["banana", "orange", "apple", "grape", "strawberry", "kiwi"]

# we want a random number between 0 and length -1

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print("A Random Fruit: {}".format(fruit))
