Even Indices
==============
Statement:
----------
Given a list of numbers, find and print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...).

```.py
# enable the input and split it 
a = input().split()  # split input to make it an array

# print the numbers with an even indice
for i in range(0, len(a), 2):
    print(a[i])
```



Even elements
============
Statement:
-----------
Given a list of numbers, find and print all elements that are an even number. In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range()

```.py

# how I solved:
for a in input().split():   
    if int(a) % 2 == 0:
        print(a)
    
# how snakify solved:
a = [int(i) for i in input().split()]  #generator
for elem in a:
    if elem % 2 == 0:
        print(elem)
```


Greater than previous
=================
Statement:
-------------
Given a list of numbers, find and print all the elements that are greater than the previous element.

```.py
# how I solved:
for i in range(len(a)-1):
    if int(a[i+1]) > int(a[i]) :
        number.append(a[i+1])
print(' '.join([str(b) for b in number])) #print the number in the array number in one line separated by spaces(' '.join)

# how snakify solved
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
```    
 
 Neighbors of the same sign
 ====================
Statement:
---------------
Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank.   
```.py
# How I solved:
a = [int(i) for i in input().split()] #generator
for n in range(len(a)-1):
    if a[n]*a[n+1] > 0:     # the multiplication of numbers of the same sign is equal to a positive number (number greater than zero)
        print(a[n], a[n+1])
        break                # after finding the first pair stop the program
        
# How snakify solved:       
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break 
 ```       
 
Greater than neighbours
=================
Statement:
---------------
Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.
The first and the last items of the list shouldn't be considered because they don't have two neighbors.
```.py

# how I solved:
b = 0
a = [int(i) for i in input().split()]

for n in range(1, len(a)-1):        # do not count the first and last number
    if a[n] > a[n+1] and a[n] > a[n-1]:   # compare 
        b = b + 1
print(b)

# how snakify solved:
a = [int(i) for i in input().split()]
counter = 0

for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)
```
