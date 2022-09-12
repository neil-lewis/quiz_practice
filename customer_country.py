import csv

def main():

    infile = open('customers.csv','r')

    outfile = open('customer_country.csv','w')

    csvfile = csv.reader(infile, delimiter = ',')

    next(csvfile)

    for row in csvfile:
        outfile.write(row[1] + ' ' + row[2])
        outfile.write(', ')
        outfile.write(row[4])
        outfile.write('\n')

    outfile.close()

main()