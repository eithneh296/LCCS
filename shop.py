import statistics
import pandas

df = pandas.read_csv('shopping_data.csv')

Amt_1 = df['Amt1']
print(Amt_1)


Amt_2 = df['Amt2']
print(Amt_2)


Amt_3 = df ['Amt3']
print(Amt_3)

mean_value = round(statistics.mean(Amt_1), 2)