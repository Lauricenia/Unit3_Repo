Question 2:
=========================
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that i is an integral number between 1 and n (both included). The program should print the dictionary.  

Sample Input:  8   
Expected Output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}   


```.py
# get input (number)
n = int(input())

# create dictionary
Dict = {}

# Store in dictionary
for i in range(1, n+1):
    Dict[i] = i ** 2

# print dictionary
print(Dict)
```
