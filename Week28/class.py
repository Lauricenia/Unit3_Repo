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
