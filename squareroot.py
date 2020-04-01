# Homework week 6
# Find the square root of 14.5
# the programme will return a square root of the number
# I originally used the math function and then following feedback from Andrew I discovered I needed to use Newton's method or my own method
# So this prompted me check online and to make changes while holding on to the original version that I used so that I could check I was right in my approach

# In my first attempts I decided I need to import the math library in order to use sqrt()
import math

y = float(14.5)

# this was the original attempt to define the function sqrt()
def sqrt(y):
    ans = math.sqrt(y)
    # round the answer to 1 decimal place
    ans = round(ans,1)
    return ans

# updated now to define the function myNewtonSqrt which will use a different method
def myNewtonSqrt(y):
    # Following feedback from Andrew I've tried using Newton's method with reference to the following three links
    # https://www.youtube.com/watch?v=2158QbsunA8
    # https://aaronschlegel.me/newtons-method-equation-roots.html
    # https://en.wikibooks.org/wiki/Think_Python/Iteration
    x = float(input("Let's find the square root of 14.5. Please enter a guess first: "))
    # so y=14.5 and x=a guess at the squareroot of y, therefore taking that guess I must  
    # first square x and subtract y
    # second multiply x by 2
    # then divide the first calculation by the second and this result is subtracted from the original best guess    
    while True:
        a = x**2 - y 
        z = 2 * x
        ans2 = x - a/z
        if abs(x - ans2) < 0.0000001: 
            break
        x = ans2
        # this answer is looped back into the first calculation to refine down the answer until the difference is less that 0.0000001
    return x

estimate = myNewtonSqrt(y)
print("Using your guess in the Newton Method the square root of", y, "is approx.", estimate) 

print("This can be rounded to", round(estimate,1))   

print("And actually using the imported square root function, the square root of", y, "is approx.", sqrt(y))
