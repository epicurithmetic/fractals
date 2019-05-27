# Mandelbrot set. Code from James Stuart
import numpy as np
from matplotlib.pyplot import *

# x and y axes to build Argand plane.
x = np.linspace(-2,1,1000)
y = np.linspace(-1,1,1000)

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

# Iterates the function.
for it in range(100):
    notdone = np.less(z.real*z.real + z.imag*z.imag, 4.0)
    output[notdone] = it
    z[notdone] = z[notdone]**2 + c[notdone]
output[output == 100-1] = 0.01

# Displays the figure.
figure = figure(figsize=[15,10])
imshow(output, cmap='hot',extent=[-2, 1, -1, 1])
show()
