
MAP
-------
```.py
import math ##because we will need to use pi

def area(r):  ##defining the function

return math.pi * (r**2)
radii = [2, 5, 7.2, 0.3, 10]

Method 1: Direct Method
=======
areas = []
for r in radii:
  a = area(r)
  areas.append(a)
print(area)

Method 2: Use map function
========
map(area, radii)
##the output will not be a list but a map object, which is actuallyan iterator over the results and we would convert it by pass the map to the list constructor:
list(map(area, radii)

Data: a1, a2, a3..., an
Function : f(a)
map(f,data):
Returns iterator over 
f(a1), f(a2), f(a3),...f(an)


FILTER
---------
import statistics module

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

list(filter(lambda x : x > avg, data))
print(filter)



#Remove missing data

vowels = [a, "", e, i, "", "", o, u]
list(filter(None,vowels)
##this filters out all values that are treated as false in a boolena setting 
False values in Python:
" ", 0, 0.0, 0j, [], (), {}, False, None, instances that signal they are empty.


reduce Function
---------------

##multiply all numbers in a list

data = [2, 5, 7, 11, 13, 17, 19, 22, 23, 29]

multiplier = lambda x,y: x*y
reduce (multiplier, data)


product= 1
for x in data:
  product = product * x
