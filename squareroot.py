# Homework week 6
# Enter a positive number - in this case 14.5
# the programme will return a square root of the number
# I originally did this without Newton Method as I wasn't aware of such a thing
# I originally used the math function and then following feedback from Andrew I discovered I needed to use Newton's method or my own method
# So this prompted me check online and to make changes while holding on to the original version that I used so that I could check I was right in my approach

# In my first attempts I decided I need to import the math library in order to use sqrt()
import math

# in order to enter a number with a decimal I need to use float()

x = float(input("Let's find the square root of 14.5. Please enter a guess first: "))

y = float(14.5)

# define the function sqrt()
def sqrt(y):
    ans = math.sqrt(y)
    # round the answer to 1 decimal place
    ans = round(ans,1)
    return ans

# define the function myNewtonSqrt which will use a different method
def myNewtonSqrt(y):
    # Following feedback from Andrew I've tried using Newton's method with reference to the following two links
    # https://www.youtube.com/watch?v=2158QbsunA8
    # https://aaronschlegel.me/newtons-method-equation-roots.html
    # so y=14.5 and x=a guess at the squareroot of y, therefore taking that guess I must  
    # first square x and subtract y
    # second mutiple x by 2
    # then divide the first calculation by the second and this result is subtracted from the original best guess 
    a = x**2 - y 
    z = 2 * x
    ans2 = x - a/z
    ans2 = round(ans2,1)
    return ans2
print("Using your guess, and the Newton Method, the square root of", y, "is approx.", myNewtonSqrt(y))    

print("And actually, the square root of", y, "is approx.", sqrt(y))
