# RANDOM - PSEUDO RANDOM NUMBER GENERATOR
# https://docs.python.org/3/library/random.html

'''
import random # importing everything in random library

# store the value of coin
coin = random.choice(["heads","tails"])  # notice the syntax of this list

print(coin)

'''


from random import choice  # for specifying which function i want to use


coin = choice(["heads", "tails"])

print(coin)
