Question 4:
============================
Define a class which has at least two methods:  

getString: to get a string from console input.     
printString: to print the string in upper case.    

Also please include a simple test function to test the class methods by instantiating an object.  


```.py
class String():
    # initiate the class
    def __init__(self):
        self.string = ""

    # first method
    def getString(self):
        self.string = input()

    # second method
    def printString(self):
        print(self.string.upper())


# initiate object
string = String()
# run functions
string.getString()
string.printString()
```
