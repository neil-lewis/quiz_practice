import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

for row in csvfile:
    print('ID: ',row[0])
    print('Full Name: ', row[1], row[2])
    print('City: ', row[3])
    print('Country: ', row[4])
    print('Phone: ', row[5])
    input('Press enter to continue\n')