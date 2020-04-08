from string import ascii_lowercase

# get input (string) and put it in a array (split)
n = input().split(",")

# create variable
text = []

# for every alphabet letter :
for letter in ascii_lowercase:
    # and every word on the input
    for i in range(len(n)):
        # compare the first letter of the word with the alphabet letter(starting from a). If different, pass to the next word
        if n[i][0] != letter:
            continue
        # if same store in the variable
        else:
            text.append(n[i])
# print the string (join)
print(','.join(text))
