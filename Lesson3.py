#Discrete random variables
import scipy.stats as st
import matplotlib.pyplot as plt

'''A university knows that 20% of its students drop out of the introductory statistics course.
Assume that 20 students enrolled in that course this quarter.'''

n = 20 #sample size
p = 0.2 #parameter

'''What is the probability that 2 or fewer drop out?'''
r = 2
prob = st.binom.cdf(r, n, p)
print(f'The probability is {prob:.2%}'.format())
print()
'''What is the probability that at most 4 drop out?'''
r = 4
prob = st.binom.cdf(r, n, p)
print(f'The probability is {prob:.2%}'.format())
print()
'''What is the probability that more than three will drop out?'''
r = 3
prob = 1 - st.binom.cdf(r, n, p)
print(f'The probability is {prob:.2%}'.format())
print()
'''What is the probability that fewer than 10 drop out?'''
r = 9
prob = st.binom.cdf(r, n, p)
print(f'The probability is {prob:.2%}'.format())
print()
'''What is the probability that between 5 and 12 students drop out?'''
r1, r2 = 12, 5
prob = st.binom.cdf(r1, n, p) - st.binom.cdf(r2-1, n, p)
print(f'The probability is {prob:.2%}'.format())
print()
'''What is the expected number of dropouts?'''
d = st.binom(n,p)
ev = d.mean()
print(f'The expected value is {ev:.2}'.format())

r_l = list(range(n+1))
pr_l = [st.binom.pmf(r, n, p) for r in r_l]
plt.bar(r_l, pr_l)
plt.show()
