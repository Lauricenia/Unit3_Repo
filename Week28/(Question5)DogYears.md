
Question 5:
================
Write a Python program to calculate a dog's age in dog's years. Go to the editor
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.


```.py
# Get input (number of human years)
Hyears = float(input())
firstyear = 10.5
# if less than 2, only use : the first 2 years correspond to 10.5 dog years each
if Hyears < 2:
    Dyears = Hyears * firstyear
# else, also use: each year after the 2 first years, equals 4 human years.
else:
    Withoutfirst = Hyears - 2
    Dyears = Withoutfirst * 4 + firstyear*2

print("The dog's age in dog's years is", Dyears)
```
