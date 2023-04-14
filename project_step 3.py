import matplotlib.pyplot as plt

data = ('Year' >= '2012') & ('Year' <= '2021')

total_sold = data.groupby(['Year' ])['Sales' ].sum()

plt.bar(total_sold.index,total_sold)

plt. title('Total Sales bv Year')
plt.xlabel('Year')
plt. ylabel('Total Sales')
plt. xlim([2012, 2021])

plt. show()