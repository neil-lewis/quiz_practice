import csv

def main():

    infile = open('clients.txt', 'r')

    csvfile = csv.reader(infile, delimiter = ',')

    i = 0
    
    for row in csvfile:
        i += 1
        print(i, '. ', row[0], sep = '')
        input('Press enter to continue\n')

main()
