
#open the txt file
file = open("extract.txt", "r")
extract = file.read()
#print extract
print(extract)

#split the text by spaces (form an array of letters in the extract)
words = extract.split()
#print array
print(words)

#print length of the array
print("Answer to Q1: ", len(words), "words")

##Question 2
#put the words to check in an array
keywords = ['house', 'worker', 'master', 'hard', 'irresponsible', 'skillful']
#make a for loop to check all the array elements
for kwd in keywords:
    #print the word you sre checking
    print("Checking the word {} in the text: ".format(kwd))
    #print if it is true or false that it exists in the extract
    print(kwd in extract)

##Question 3
name = 'john'
print(f"hello {name}")

countAlpha = 0
for letter in extract:
    if letter.isalpha():
        countAlpha += 1

print(f'there are {countAlpha} letters (a-z) out of {len(extract)} total')

##Question 4
#make the text lowercase
print(extract.lower())


##Question 5

#make a list of numbers
#filter the false conditions
#you get a function only with words with length 5
wordsLong= list(filter(lambda x: len(x) > 5, words))

#print the length of list (how many numbers with 5 characters we have)
print(len(wordsLong))
#print the words with length greater than 5 with #appended in the infront of each word
print('#'.join(wordsLong))

##Question 6
## summing the numeric representations of the letters in the extract
total = 0
for letter in extract:
    #convert the letter to the ascii code
    total += ord(letter)
print(total)
