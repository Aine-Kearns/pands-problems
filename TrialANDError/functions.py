# a function to square numbers.
# modified to include other functions and identify the difference of functions and algorthm 

import math

def power(x, y): 
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans

def f(x):
    ans = (100 * power(x, 2) + 10 * power(x, 3)) // 100 
    ans = ans - (power (x, 3) // 10)
    return ans


def isprime(i):
        # loop through all values j from 2 up to but not including i.
    for j in range(2, math.floor(math.sqrt(i))):
        # see if j divides i
        # this can actually be changed to "for j in P:" and 
        # it will avoid the second loop within the first loop and reduce the workload
        # in doing this it only loops through the prime numbers that were already generated in the loop
        if i % j == 0:
            # if it does, i isn't prime so exit the loop and indicate it's not prime
            isprime = False
            #break will take you out of the loop but if we use "continue"
            # it's like break, break breaks you out of the loop but continue will stop everything under neath being executed
            # but it will keep the loop alive
            return False
    return True 