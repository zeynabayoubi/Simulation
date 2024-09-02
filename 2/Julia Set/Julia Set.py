import numpy as np
import matplotlib.pyplot as plt


def julia_set(c= -0.4 + 0.6j, height=800, width=1000, x=0, y=0, max_iterations=100):
    
    x_width = 1.5
    y_height = 1.5*height/width
    x_start= x - x_width
    x_end = x + x_width
    y_start = y - y_height
    y_end = y + y_height

    
    x = np.linspace(x_start, x_end, width).reshape((1, width))
    y = np.linspace(y_start, y_end, height).reshape((height, 1))
    z = x + 1j * y

    
    c = np.full(z.shape, c)
    div_time = np.zeros(z.shape, dtype=int)
    m = np.full(c.shape, True, dtype=bool)
    

    for i in range(max_iterations):
        z[m] = z[m]**2 + c[m]

        m[np.abs(z) > 2] = False

        div_time[m] = i
    return div_time


plt.imshow(julia_set(), cmap='magma')
plt.title('This picture is for c= -0.4 + 0.6i ',fontweight ="bold")

plt.show()
