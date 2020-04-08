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