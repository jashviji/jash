import matplotlib.pyplot as plt

with open('stats.txt', 'r') as f:
    lines = f.readlines()
    estimated_sales = {}
    for i in range(len(lines)):
        if 'Estimated sales for last six months of 2022: ' in lines[i]:
            for j in range(i+1, len(lines)):
                month_sales = lines[j].strip().split(': ')
                month = int(month_sales[0])
                sales = float(month_sales[1])
                estimated_sales[month] = sales

plt.figure = plt.subplots(figure=(8, 4))
plt.barh(list(estimated_sales.keys()), list(estimated_sales.values()))
plt.title('Estimated Sales for last six Months of 2022')
plt.xlabel('Estimated Sales')
plt.ylabel('Month')
plt.grid()

plt.show()