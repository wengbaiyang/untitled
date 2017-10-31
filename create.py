print sum(i*i for i in range(10))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print sum(x*y for x,y in zip(xvec, yvec))

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print sine_table
