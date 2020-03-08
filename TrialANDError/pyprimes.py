# computing the primes

from functions import isprime
             
# my list of primes - TBD
P = []

#Loop through all of the nubmers we're checking for primality.
for i in range(2,100000):
    #if i is prime, then append to P
    if isprime(i):
        P.append(i)

#Print out our list
print(P)