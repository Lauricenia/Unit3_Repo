text = input("Please enter your first and last name and a number from 1 to 100")
nr = int(text.split(",")[2]) # input number
namesEmail = text.split(", ")[0] + "." + text.split(", ")[1]  # first part of the email

if nr > 100:
    print("Please input a number that is less than 100(not included) and greater than 1(included)")

f = open("output.txt", "w")  # open file

for n in range(1, nr+1):
    # print(namesEmail.lower() + str(n) + "@.uwcisak.jp")
    f.write(namesEmail.lower() + str(n) + "@.uwcisak.jp \n")  # write on file

f.close()  # close file