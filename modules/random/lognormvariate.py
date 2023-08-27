#Based on a log-normal distributon, used n probablity theories
import random

MU = 1
SIGMA = 4
NORMALVARIATE = random.lognormvariate(mu=MU, sigma=SIGMA)

# output
print(NORMALVARIATE) # No Format
print(f"{NORMALVARIATE:.2f}") # Formatted