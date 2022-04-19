import numpy as np
from astropy import units as u

file1 = open('/home/jack.moreland/AST4930/HW7/sed.txt', 'r')
data = np.loadtxt(file1, delimiter = ',')

x = data[:, 0] * (u.micron)
y = data[:, 1] * (u.Lsun/u.micron)

mask = (data[:, 0] >= 10) & (data[:, 0] <= 1000)

newdata = data[mask]

x = newdata[:, 0] * (u.micron)
y = newdata[:, 1] * (u.Lsun)/(u.micron)
x = np.flip(x)
y = np.flip(y)

value = np.trapz(y, x)
value = value.to(u.erg/u.s)
print(value)

