import csv

def main():

    infile = open('employeepay.csv', 'r')

    csvfile = csv.reader(infile, delimiter = ',')

    next(csvfile)

    for row in csvfile:
        print('ID:', row[0])
        print('Name:', row[1], row[2])
        print('Base Salary: ', '$', format(float(row[3]),',.0f'), sep = '')
        print('Bonus: ', format(float(row[4]) * 100,'.0f'), '%', sep = '')
        print('Total Compensation: ', '$', format(((float(row[3]) * float(row[4])) + float(row[3])),',.2f'),sep = '')
        input('Press enter to continue\n')

main()