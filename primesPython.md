
These file shows the different versions and explanations of the program for finding a prime number using python. The testing of different versions was to find a version that takes less time to find the prime number. 

Version 1
--------------
This version is the slowest.
```.py
def is_prime_v1(n): ##defining function
  if n == 1:
   return False 
  for d in range(2,n):
    if n % d == 0:
      return False
  return True

for n in range (1, 21):
  print(n,is_prime_v1(n))
```

Explanation:
=======

1. Number one is never a prime number so we eliminate the possibility right away
  ```.py
  if n == 1:
    return False 
  ```

2. Test if the number is divisible by any number less than it starting from 2. We dont start from 1 because all the numbers are divisible by 1. If the condition is not true for the number, then it is a prime number (return True).
```.py
  for d in range(2,n):
    if n % d == 0:
      return False
  return True
 ```
 This version takes a lot of time because it checks for all the numbers less than the integer that we are checking. The next program shows how to solve this problem.
  
  
Version 2:
----------
```.py
import math

def is_prime_v2(n):
  if n == 1:
   return False 

  max_divisor = math.floor(math.sqrt(n))
  for d in range(2,1 + max_divisor):
    if n % d == 0:
      return False
  return True

for n in range (1, 21):
  print(n,is_prime_v2(n))
 ```
 Explanation:
 =======
    
1. Factors of a non-prime number repeat themselves after the multiplication of it's square roots. This shows us that there is no need to check for all the numbers because it is the same thing as checking up to the square root of the number.
```.py
max_divisor = math.floor(math.sqrt(n))
  for d in range(2,1 + max_divisor):
    if n % d == 0:
      return False
  return True
  ```
 2. This program uses less time than the version before but can still be improved. If we find that the number to check is an even number, it cannot be a prime number. And so we are left with the odd numbers that can only have odd factors. Tdecreases the number of options to be checked and so decreases the time of execution of the program.
  
  Version 3
  -------------
  ```.py
  import math
  import time

def is_prime_v3(n):
  if n == 1:
   return False 

  if n > 2 and n % 2 == 0:
   return False

  max_divisor = math.floor(math.sqrt(n))
  for d in range(3, 1 + max_divisor, 2):
     if n % d == 0:
        return False     
  return True

for n in range (1, 21):
  print(n,is_prime_v3(n))
  
 ```
 Explanation
=========
 1. If a number is greater than two and its even,it is a non-prime number. This saves the time used for checking the numbers for even numbers.
   ```.py
   if n > 2 and n % 2 == 0
   return False
   ```
   
 2. This one is for the case of the number being an odd, we start on 3(because its an odd number) and test for other odd numbers (step value = 2, this step value jumpes the even numbers)
 ```.py
 max_divisor = math.floor(math.sqrt(n))
  for d in range(3, 1 + max_divisor, 2):
     if n % d == 0:
        return False     
  return True
  ```
    
  
  Function used to check time
  ------------
  ```.py
T0 = time.time()
for n in range (1, 100000):
  is_prime_v1(n)
T1 = time.time()
print(T1 - T0)
  ```
  
  
  
  
