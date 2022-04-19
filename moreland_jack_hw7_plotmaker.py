import numpy as np
import matplotlib.pyplot as plt

file1 = open('/home/jack.moreland/AST4930/HW7/sed.txt', 'r')
data = np.loadtxt(file1, delimiter = ',')

x = data[:, 0]
y = data[:, 1]

fig, yx1 = plt.subplots(1, 1)
fig.set_size_inches(6, 4)

yx1.plot (x, y)
yx1.set_xscale('log')
yx1.set_yscale('log')
yx1.set_ylabel('specific luminosity')
yx1.set_xlabel('microns')

fig.savefig('moreland_jack_hw72.png')
