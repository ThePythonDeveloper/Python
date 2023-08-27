# Based on the von Mises disturbution (used in directioal statistcs)
import random

MU = 2
KAPPA = 4
von = random.vonmisesvariate(mu=MU, kappa=KAPPA)

# output
print(von) # No Format
print(f"{von:.2f}") # Formatted