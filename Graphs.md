Graph1
------------
① f(x) = (x+1)^2 - 1, with x from -2, to 2 with 1000 points
```.py
import matplotlib.pyplot as plt

min = -2  # set the minimum numbers of the x array
x = [min]  # add the minumm to the x array
y = []

for i in range(999):
    x.append(min+4/999*(i+1))   # add the other 999 numbers to the x array (the last number must be 2)

y = [((i+1)**2 - 1) for i in x]     # for each number in x apply the formula

# plot the graph 
plt.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')

plt.show()
```



Graph 2
--------------
② [HL] g(x) = 0.1*sin(0.1*m(x)), where m(x) = x^2, and x from 0 to 30 with steps of 0.05
```.py
from math import sin
import matplotlib.pyplot as plt


min = 0     # set the minimum numbers of the x array
x = [min]     # add the minumm to the x array
m = []
g = []

for i in range(600):
    x.append(min+0.05*(i+1))  # set the other x numbers by a step of 0.05 till x = 30

m = [a**2 for a in x]     # for the values in x apply this formula

g = [0.1*sin(0.1*n) for n in m]  # for the values in m apply this formula

# plot the graph
plt.plot(x,g)

plt.xlabel('x')
plt.ylabel('g')

plt.show()
```

