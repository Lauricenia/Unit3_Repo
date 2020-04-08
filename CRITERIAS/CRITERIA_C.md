To develop the inventory, I broke down the big problems into smaller ones, easier to tackle.
I thought of what would be the user experience with the app in steps. My thinking was that: First, the user would open the app and the first 
thing to take into account is security and for this reason, the first user interface I started designing was the **Login window**. The other windows were designed following the same type of thinking. 
The order of the design is the same as the order I used to show the UI captures in Section B.

After the UI designs were complete, the next step of the development started : coding the User Interfaces. 
This big step was also divided in a logical set of small tasks : 
1. Convert the UI pages into python code

1. Creating Classes
```.py
class LogInApp(loginD):
    def __init__(self, parent=None):
        super(LogInApp, self).__init__(parent)
        self.setupUi(self)
```  
1. Buttons
```py
 # behaviour for the cancel button
        self.cancel.clicked.connect(self.exitApp)
        # open the register window
        self.Register.clicked.connect(self.regApp)
        # login
        self.LogIn.clicked.connect(self.try_login)
 ```
1. Connecting windows
```.py
     def regApp(self):
        regVar = RegisterPage(self)
        regVar.show()
```
        
1. Reading and writing values on a table
```.py
        with open('db.csv') as mydatabase:
            file = csv.reader(mydatabase, delimiter=",")
            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col))
        return []
  ```


...etc

After all Ui were converted, I realised the coding for each file was very long. Working like this would difficult the code writing and make the algorithms less readable, specially if I had decided to code the files separately. 
For this reason, I opened a new python file to write the code that would allow me to code and run all the UI at the same time and would make the code more 
readable and prevent less typos or unintentional erasing or editing of important code in the converted UI files.

**importing the code from the different UI into one file**
```.py
from Login_page import Ui_LoginForm as loginD
from Recent_changes_page import Ui_MainWindow as mainW
from Register_page import Ui_Register as reg
from main_records import Ui_Records as rec
```
This method allows me to create the classes and to only call the components I want to code. The classes for the windows are done in the same type of way. 
