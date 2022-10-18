#Probability
import pandas as pd

'''A store has 300 balls for sale, of which 100 are red and the rest are blue.
Of the red ones, 20% are basketball and the rest are soccer. Knowing that there are 250 footballs'''

balls = 300 #sample size
colors = ['red','blue','total']
red = 100
blue = 200

#Game
games = ['football','basket']
football = 250
basket = 50

rb = 20
rf = 80
bf = 170
bb = 30

balls_df = pd.DataFrame(index = colors, columns= games)
balls_df['football'] = [rf,bf,rf+bf]
balls_df['basket'] = [rb,bb,rb+bb]
balls_df['total']=balls_df['football']+balls_df['basket']
print(balls_df)

print()
'''Find the probability that a randomly chosen ball, either blue or basketball.'''
prob_1 = (balls_df['total']['blue'] + balls_df['basket']['total'] - balls_df['basket']['blue']) / balls
print(f'The probability is {prob_1:.2%}'.format())
print()
'''Find the probability that a randomly chosen ball, either blue and football.'''
prob_2 = (balls_df['football']['blue']) / balls
print(f'The probability is {prob_2:.2%}'.format())
print()
'''Is the color independent of the game?'''
if prob_2 == (balls_df['football']['total']*balls_df['total']['blue'])/(balls)**2:
    indep = 'is'
else:
    indep = 'is not'
print(f'The color {indep} independent of the game')
