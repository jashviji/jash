import csv

with open ('Data.csv', mode='r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    for line in fCSV:
        print(line)


print('\n--------------------------\n')

data_filtered = ('Year' >= '2012') & ('Year' <= '2021')

total_sold = data_filtered.groupby(['Year'])['Sales'].sum()

with open('stats.txt', 'W') as f:
    for year, sales in total_sold.items():
        f.write(f'(year): (sales)\n')
