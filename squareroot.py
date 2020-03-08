# Enter a positive number
# the programme will return a square root of the number

# need to import the math library in order to use sqrt()
import math

# in order to enter a number with a decimal need to use float()

x = float(input("Please enter a number: "))

# define the function sqrt()
def sqrt(x):
    ans = math.sqrt(x)
    # round the answer to 1 decimal place
    ans = round(ans,1)
    return ans

print("The square root of", x, "is approx.", sqrt(x))
    


