# Based on the normal disburtion, used in probablity theories
import random

MU = 1
SIGMA = 4
NORMAL = random.normalvariate(mu=MU, sigma=SIGMA)

# output
print(NORMAL) # No Format
print(f"{NORMAL:.2f}") # Formatted