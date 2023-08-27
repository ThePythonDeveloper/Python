# these names sound like someone used a random word generator

# based on the weibull distributon (used in statstics)

import random

ALPHA = 3 # replace with your alpha number here
BETA = 5 # replace with your beta number here
wei = random.weibullvariate(alpha=ALPHA, beta=BETA)

# outputs
print(wei) # No Format
print(f"{wei:.2f}") # Formatted