#Continuous random variables
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

'''A person with a good credit rating has an average debt of $15,015.
Assume that the standard deviation is $3,540 and that the debt amounts are normally distributed.'''

mu = 15015
sd = 3540

'''What is the probability that the debt of a person with a good credit rating is greater than $18,000?'''
x = 18000
prob = 1 - st.norm.cdf(x, mu, sd)
print(f'The probability is {prob:.2%}'.format())
print()

'''That the debt of a person with a good credit rating is less than $10,000?'''
x = 10000
prob = st.norm.cdf(x, mu, sd)
print(f'The probability is {prob:.2%}'.format())
print()

'''That the debt of a person with a good credit rating is between $12,000 and $18,000?'''
x1,x2 = 12000, 18000
prob = st.norm.cdf(x2, mu, sd) - st.norm.cdf(x1, mu, sd)
print(f'The probability is {prob:.2%}'.format())
print()

'''That the debt of a person with a good credit rating is greater than $14,000?'''
x = 14000
prob = 1 - st.norm.cdf(x, mu, sd)
print(f'The probability is {prob:.2%}'.format())
print()

x = np.random.normal(mu, sd, 10000)
plt.hist(x,100)
plt.show()
