
MAP FUNCTION
========
```.py
import math ##because we will need to use pi

def area(r):  ##defining the function

return math.pi * (r**2)
radii = [2, 5, 7.2, 0.3, 10]

...
```

Method 1: Direct Method
-------
```.py
areas = []
for r in radii:
  a = area(r)
  areas.append(a)
print(area)
```
1. This method uses a for loop to calculate the area for all the radii in the array 

Method 2: Use map function
-------
```.py
map(area, radii)
```
2. This method uses the map funtion to calculate the area for all the radii in the array. The output will not be a list but a map object, which is actually an iterator over the results. To convert it we passthe map to the list constructor:
```.py
list(map(area, radii))
```

**General formula:**
```
Data: a1, a2, a3..., an
Function : f(a)
map(f,data):
Returns iterator over 
f(a1), f(a2), f(a3),...f(an)
```

FILTER FUNCTION
========
```.sh
import statistics module ##because we will be using mean

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

list(filter(lambda x : x > avg, data))
print(filter)

```
1. the list function filters the data according to the condition. For this case it outlines data that is larger than the average 
```.py
list(filter(lambda x : x > avg, data))
print(filter)
```
*lambda: Is an anonymous function (a function is without a name). This function can have any number of arguments but only one expression, which is evaluated and returned.*

Remove missing data(special example)
--------

```.py
vowels = [a, "", e, i, "", "", o, u]
list(filter(None,vowels))
```
2. This filters out all values that are treated as false in a boolena setting 

```
False values in Python:
------------------
" ", 0, 0.0, 0j, [], (), {}, False, None, instances that signal they are empty.
```


REDUCE FUNCTION
========
```.py
import functools

data = [2, 5, 7, 11, 13, 17, 19, 22, 23, 29]

multiplier = lambda x,y: x*y
reduce(multiplier, data)
```
1. This uses the reduce function to multiply all numbers in a list.

```.py
product= 1
for x in data:
  product = product * x
  ```
2. However using the for loop fucntion would make the program more readable
