# Julia set animation.
import timeit
import os
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# On your marks. Get set. Go...
start = timeit.default_timer()

fig = plt.figure()
plt.axis('off')

# x and y axes to build Argand plane. This controls resolution of the image.
x = np.linspace(-1.5,1.5,500)
y = np.linspace(-1,1,500)

# List of parameters to control the varying Julia sets.
parameters = np.linspace(0,2*np.pi,500)

# List of images
images = []

count = 0
for t in parameters:

    # Argand plane.
    c = x[np.newaxis,:] + 1j*y[:,np.newaxis]


    # The image file.
    output = np.zeros(c.shape)

    # This for-loop updates the output file
    for it in range(100):
        notdone = np.less(c.real*c.real + c.imag*c.imag, 4.0)
        output[notdone] = it
        # The line below determines which function we use:
        # Customisation can be done by changing the right-hand side of the
        # equation i.e. power of z and the constant factor. 
        c[notdone] = c[notdone]**2 + complex(0.285,0.01)*cmath.exp(1j*t)
    output[output == 100-1] = 0.01

    # Animation needs an image, not an array of numbers.
    # Before we can animate, we have to turn each array into an image.
    plt_im = plt.imshow(output, cmap='hot',extent=[-1.5, 1.5, -1, 1], animated = True)


    # This block is here for viewing purposes. To give an idea of how long
    # the process will take once running. Updates viewer everytime an image
    # is processed and put into the list of images.
    os.system("cls")
    print 'There are %d remaining images to process' % (len(parameters) - count)
    images.append([plt_im])
    count += 1

#... Finshed.
print 'All data uploaded to the list.'
stop = timeit.default_timer()
print 'Time: ', stop - start


# ArtistAnimation does all of the stiching together of the frames for us.
ani = animation.ArtistAnimation(fig, images, interval=1000./50., blit=True,
                                repeat_delay=0)

### DO NOT OVERWRITE!!!
#plt.savefig('julia_ani2.png')
ani.save('julia_ani_explore.mp4', writer='ffmpeg', fps=20)
plt.show()
