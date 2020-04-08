[HL]　Data Analysis
=====================
 
① Follow the video tutorial “HL Data Analysis” that shows how to plot a CSV file with Python.  
② Download the CSV file for Total confirmed cases (WHO) and create a scatter plot where the x-axes is the number of days, and the y axes is the total number of cases confirmed.  
③ Add another line with the total number of cases in your country. That is, you will have one graph with two lines.  




```.sh
import matplotlib.pyplot as pyplot
import csv

# open csv file
with open('total_cases.csv') as dt:
    # create variable
    data = []
    # read file
    values = csv.reader(dt, delimiter=",")
    # store values in variable
    for row in values:
        data.append(row)

# atribute values to the variables
x = data[0]
y1 = data[1]
y2 = data[2]

# create a graph
pyplot.plot(x, y1, label='world')             # tried to add label for lines and it didnt work
pyplot.plot(x, y2, label='Mozambique')

# title for the axis
pyplot.xlabel('days')
pyplot.ylabel('confirmed cases')

# Show graph
pyplot.show()
```
