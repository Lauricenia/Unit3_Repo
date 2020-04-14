import matplotlib.pyplot as pyplot
import csv
from scipy.stats import pearsonr

# open csv file
with open('data.csv') as dt:
    # create variable
    data = []
    # read file
    values = csv.reader(dt, delimiter=",")
    # store values in variable
    for row in values:
        data.append(row)

# atribute values to the variables
x = [int(d) for d in data[0]]
y = [int(d) for d in data[1]]

corr, p_value = pearsonr(x, y)

print(corr)

# create a graph
pyplot.scatter(x, y)

# title for the axis
pyplot.xlabel('number of cases')
pyplot.ylabel('price of gold')

# Show graph
pyplot.show()
