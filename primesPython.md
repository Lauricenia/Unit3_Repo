
These file shows the different versions and explanations of the program for finding a prime number using python. The testing different versions was an attempt to find the program that takes less time possible to find the prime number. 

Version 1
--------------
This version is the slowest (takes a lot of time)

def is_prime_v1(n):

  .sh" if n == 1:
    return False " #1 is not prime

  for d in range(2,n):
    if n % d == 0: #test if it is divisible by any number less than it, from the number 2 because all numbers are divisible by 1.
      return False
  return True
  
  
Version 2:
----------
import math 
  def is_prime_v2(n):
  if n == 1:
    return False #1 is not prime
    
  #there is no need to test all the numbers because the factors of a non-prime number repeat themselves after the square root of the number.
  max_divisor = math.floor(math.sqrt(n))
  for d in range(2,1 + max_divisor):
    if n % d == 0:
      return False
  return True
  
  def is_prime_v3(n):
   if n == 1:
    return False #1 is not prime
  
  #if a number is greater than two and its even,it is a non-prime number. This saves the time used for checking the numbers.
   if n > 2 and n % 2 == 0
   return False
   
   #this one is for the case of the number being an odd, we start on 3(because its an odd number) and test for other odd numbers (step value = 2, this step value jumpes the even numbers)
 max_divisor = math.floor(math.sqrt(n))
  for d in range(3, 1 + max_divisor, 2):
     if n % d == 0:
        return False     
  return True
    
  
   
  
  
  
