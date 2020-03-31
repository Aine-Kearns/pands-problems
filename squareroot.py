# Homework week 6
# Enter a positive number - in this case 14.5
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

def mySqrt(x):
    # Using Newton's method with reference to the following two links
    # https://www.youtube.com/watch?v=2158QbsunA8
    # https://aaronschlegel.me/newtons-method-equation-roots.html
    # so y=sqrt(14.5), therefore y-(sqrt(14,5))=0, therefore (y**2 - 14.5) + 1 = 1 so 
    y = x**2 - 2 
    #it cant be x = 14.5 here x is the best guess
    z = 2 * x
    ans2 = x - y/z
    return ans2
print("The square root of", x, "is approx.", mySqrt(x))    


