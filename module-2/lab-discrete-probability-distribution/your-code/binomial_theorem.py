from math import factorial
# n: total events
# k: successful events, must be less or equal than n
# p: probability of success or rate, between 0 and 1
def binomial_theorem(n, k, p):
    return factorial(n) / (factorial(k) * factorial(n-k)) * p**k * (1 - p)**(n-k)
