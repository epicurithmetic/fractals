# Julia set.

# Julia sets are beautiful fractals constructed in the complex plane.
# Discovered by Gaston Julia - French mathematician - and made popular by
# Benoit Mandelbrot - French mathematician.

# One way to understand these images is as the the "rate of escape" of a
# given point under the given function.

import numpy as np
import math
import cmath
from matplotlib.pyplot import *

# x and y axes to build Argand plane.
x = np.linspace(-1.5,1.5,500)
y = np.linspace(-1,1,500)

# Argand plane.
c = x[np.newaxis,:] + 1j*y[:,np.newaxis]

# Note: np.newaxis is used in order to get each y value above each x value. If
# x and y were added without np.newaxis, they would just get added component-wise.
# thus yielding the diagonal line in the Argand plane.

# An array of zeroes in the same shape as c. Entries are complex numbers.
z=np.zeros(c.shape,dtype=np.complex64)
# An array of zeroes in the same shape as c. Entries are integers.
output = np.zeros(c.shape)

# np.less returns Boolean based on an inequality i.e. a<b == np.less(a,b).

# notdone stores whether or not the quadrature of the imaginary numbers in z
# is (strictly) less than 4.
### notdone = np.less(z.real*z.real + z.imag*z.imag, 4.0)

# Set a paramter to change the function and hence change the plot:
# z = z^2 + 0.7885exp(ia) --- where a in {0,2pi} parameterizes the fractals.
# Particularly interesting Julia sets occur at a = {1.65, 1.85, ...}
a = 1.85

# Iterates the function on the domain.
for it in range(100):
    notdone = np.less(c.real*c.real + c.imag*c.imag, 4.0)
    output[notdone] = it
    # The line below determines which function we use:
    c[notdone] = c[notdone]**2 + 0.7885*cmath.exp(1j*a)
output[output == 100-1] = 0.01

# Displays the figure.
figure = figure(figsize=[15,10])
axis('off')
title('z = z**2 + 0.7885exp(1.85i)')
# Color maps: 'gray'and 'hot' are best.
imshow(output, cmap='hot',extent=[-1.5, 1.5, -1, 1])
savefig('julia1_withEQ.png')
show()
