# copied file from IPython log file

import numpy as np
# import numpy 
import matplotlib.pyplot as plt
# import matplotlib

x = np.arange(0.0, 4.25, 0.25)
# need to define the top end at 4.25 to include 4 in the list
print(x)
# define x as a list
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
plt.show()

