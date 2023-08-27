# Based on the gaussian distribution, used in probablity theories
import random

MU = 3 # replae with your number
SIGMA = 5 # repalce with your number
GAUSS = random.gauss(mu=MU, sigma=SIGMA)

# output
print(GAUSS) # No Format
print(f"{GAUSS:.2f}") # Format