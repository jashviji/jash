sales_2021 = data.loc[data['Year'] == 2021].loc[data['Month'] <= 6,'Sales'].sum()
sales_2022 = data.loc[data['Year'] == 2022].loc[data['Month'] <= 6,'Sales'].sum()

SGR = (sales_2022 - sales_2021) / sales_2022

with open('stats.txt', 'w') as f:
    f.write(f';SGR: {SGR}\n')

estimated_sales = {}
for month in range(7, 12):
    sales_2021_month = data.loc[data['Year'] == 2021].loc[data['Month'] == month, 'Sales'].sum()
    estimated_sales[month] = sales_2021_month + (sales_2021_month*SGR)

with open('stats.txt', 'w') as f:
    f.write('Estimated Sales for last six months of 2022: ')
    for month, sales in estimated_sales.items():
        f.write(f'{month}: {sales}\n')
