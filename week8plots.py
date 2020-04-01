# Homework from week 8
# a programme that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

import numpy as np
# import numpy 
import matplotlib.pyplot as plt
# import matplotlib

x = np.arange(0.0, 4.0, 0.05)
# define x as a list and decided to use 0.05 as intervals to give the dots a clearer line
f = x
# define f(x) = x
g = x**2
# define g(x) = x**2
h = x**3
# define h(x) = x**3

plt.plot(f, f, "g.", label="x")
# plot of x by x in green
plt.plot(f, g, "r.", label="x_squared")
# plot of x squared in red
plt.plot(f, h, "b.", label="x_cubed")
# plot of x cubed in blue

plt.legend()
plt.title("Homework Week 8 - plots")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

