#Linear Regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

'''A company wants to make predictions of the amount of its total sales in a certain country from the relation to GDP.
To investigate the relationship, you have the following data:'''

y = [189, 190, 208, 227, 239, 252]  # Sales in thousands
x = [402, 404, 412, 425, 429, 436]  # GDP in millions

'''Estimate the linear correlation coefficient and interpret it.'''
rho = np.corrcoef(x,y)[0,1]
if rho > 0:
    r = 'direct'
else:
    r = 'inverse'
print(f'The correlation is {rho:.2%} and the relationship is {r}'.format())
print()

'''Estimate the line of the linear regression model'''
model = LinearRegression()
x = np.array(x)
y = np.array(y)
plt.scatter(x, y)
plt.legend(['observations'])

X = np.array(x).reshape(-1, 1)
model.fit(X, y)

b0 = model.intercept_
b1 = model.coef_[0]
print(f'Sales = {b0:.2f} + {b1:.2f} GDP + ε'.format())
print()

ym = model.predict(X)
plt.plot(x, ym, '--m')

'''If for next year a GDP of 325 millions is estimated.
What will be the forecast for the company's sales in that year?'''
xf = 325
Xf = np.array(xf).reshape(-1, 1)
yf = model.predict(Xf)[0]
print(f'The predicted sales are {yf:.2f} thousand'.format())

plt.show()
