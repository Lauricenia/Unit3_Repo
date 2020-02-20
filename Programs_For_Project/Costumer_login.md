```.py
customer1 = {'FirstName': 'Filip', 'age': 18, 'LastName': 'Keitaro', 'AccountNumber': 0o00001, 'PIN': 1119, 'Balance': 5, 'Contact': 'filip@keitaro.jp'}

def deposit(CustomerDict, Amount):
    # This function deposits amount in the customer dictionary
    CustomerDict['Balance'] += Amount
    print(f'New balance is {CustomerDict["Balance"]}')

def checkbalance(CustomerDict):
    print(f'New balance is {CustomerDict["Balance"]}')

def withdraw(CustomerDict, Amount):
    CustomerDict['Balance'] -= Amount
    print(f'New balance is {CustomerDict["Balance"]}')
    ```
