Question 1
===============

```.py
# random the values for the y-axis inside the range of 0 to 100      
y = [random.randint(0,100) for number in x]                          
                                                                     
# another way of solving(longer code):                               
# x = list()                                                         
# y = list()                                                         
# for i in range(0, 1001):                                           
# x.append(i)                                                        
# y.append(random.randint(0,100))                                    
print(x)                                                             
                                                                     
# create graph                                                       
plt.plot(x,y)                                                        
                                                                     
# label the axis                                                     
plt.xlabel('x')                                                      
plt.ylabel('y')                                                      
                                                                     
#show the graph                                                      
plt.show()   
``` 


Question 2
===============

```.py
import random

# create variable
sum = 0
# create the values for the x-axis
x = [number for number in range(1, 1001)]

# random the values for the y-axis inside the range of 0 to 100
y = [random.randint(0, 100) for number in x]

# loop for the addition of the random numbers
for i in range(0,999):
    sum += y[i]

# print the average
print(sum/1000)
```

Question 3
=================

```.py
from math import sin

import matplotlib.pyplot as plt

# https://pynative.com/python-range-for-float-numbers/ # (nymPy)

min = -10
x = []
y = []
for i in range(2000):
        x.append(min + 0.01*(i + 1))
        y.append(14*sin(0.5 * x[i]))

plt.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')

plt.show()
```

Question 4
==============

```.py
from math import log
import matplotlib.pyplot as plt

x = [i for i in range(1, 100)]

# logarithm function
y = [log(i, 2) for i in x]

# create graph
plt.plot(x, y)

# label the axis
plt.xlabel('x')
plt.ylabel('y')

# show the graph
plt.show()
```

Question 5
==============

```.py
import random                                                    
                                                                                                                                  
# random the values for the y-axis inside the range              
y = [random.randint(0, 100) for number in range(0, 1000)]        
                                                                 
# print array                                                    
print(y)                                                         
                                                                 
# bubbles sort                                                   
for number in range(1000-2):                                     
    for i in range(1000-1):                                      
        if y[i] > y[i + 1]:                                      
            store = y[i]                                         
            y[i] = y[i + 1]                                      
            y[i + 1] = store                                     
                                                        
```                                                                 
