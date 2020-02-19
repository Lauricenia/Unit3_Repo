
message = input("Enter your message here: ")
key = int(input("Enter the number to add here: "))
for word in message:
    convrt= ord(word)
    convrt+=key
    print(chr(convrt))
##short VERSION:
 print(''.join(map(ord(message)+key)))
