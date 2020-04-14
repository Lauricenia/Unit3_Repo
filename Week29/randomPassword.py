import random
import string

repeat = int(input())

for nr in range(1, repeat + 1):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    print("Password" + str(nr) + ": " + ''.join(random.choice(password_characters) for i in range(20)))
