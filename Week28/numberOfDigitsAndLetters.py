# Write a Python program that accepts a string and calculate the number of digits and letters.

# variables for counting
countlt = 0
countdg = 0

# split the input into a list
word = [chr for chr in input()]

# for loop to count
for char in word:
    # if char is a digit
    if char.isdigit():
            countdg+=1
    # if char is letter
    if char.isalpha():
            countlt+=1

# print results
print("Letters:", countlt)
print("Digits:", countdg)



