#Confidence interval
import scipy.stats as st
import numpy as np


'''In a random sample of 50 articles from a population in which σ = 6, the sample mean was 32.'''
n = 50
sd = 6
m = 32

'''Set a 90% confidence interval for the population mean.'''
confidence = 0.9
IC = st.t.interval(confidence,n,m,sd)
print(f'The IC at {confidence:.0%}'.format(), f'is %0.2f and %0.2f' % IC)
print()

"95% confidence interval?"
confidence = 0.95
IC = st.t.interval(confidence,n,m,sd)
print(f'The IC at {confidence:.0%}'.format(), f'is %0.2f and %0.2f' % IC)
print()

"99% confidence interval?"
confidence = 0.99
IC = st.t.interval(confidence,n,m,sd)
print(f'The IC at {confidence:.0%}'.format(), f'is %0.2f and %0.2f' % IC)
