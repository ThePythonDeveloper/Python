# Based on the Pareto disturbution (used in directioal statistcs)
import random

ALPHA = 3 # replace with your alpha
pareto = random.paretovariate(alpha=ALPHA)

# output
print(pareto) # No Format
print(f"{pareto:.2f}") # Formatted