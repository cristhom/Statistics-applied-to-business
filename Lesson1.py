# Descriptive statistics
import numpy as np
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt

'''The per capita income of a given population is studied for which a sample of 200 people is taken,
obtaining the following result:'''

freq = 500
min = 1000
sup = 3000

quantity = [40, 50, 100, 10]

intervals = pd.interval_range(start=min, freq=freq, end=sup, name='Income', closed='left')
income_df = pd.DataFrame(index = intervals)
income_df['frequency'] = quantity
income_df['Class Mark'] = income_df.index.mid

print(income_df)

m = sum(income_df['frequency']*income_df['Class Mark'])/sum(income_df['frequency'])

data = []
income = list(income_df['Class Mark'])

for i,q in zip(income, quantity):
    for x in range(q):
        data.append(i)

print()
print('Sample size: ', len(data))
'''Calculate the measures of center position'''
print('Mean: ', m)
print('Mode: ', stat.mode(data))
print('Median: ', stat.median(data))
print()
'''Calculate the measures of relative position'''
print('Q1 quantile: ', np.quantile(data, .25))
print('Q2 quantile: ', np.quantile(data, .50))
print('Q3 quantile: ', np.quantile(data, .75))
print()
'''Is the mean representative of the study data?'''
sd = stat.stdev(data)
print('Standard deviaton: ', round(sd,2))
if sd / m < 0.1:
    r = 'is'
else:
    r = 'is not'
print(f'The mean {r} representative')

plt.hist(data, bins=4, color='grey')
plt.show()
