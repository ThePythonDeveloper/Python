# Used in statistics also, based on the gamma disburtion
import random

ALPHA = 1 # replace with your number
BETA = 4 # replace with your number
GAMMA = random.gammavariate(alpha=ALPHA, beta=BETA)

# OUTPUT
print(GAMMA) # No Format
print(f"{GAMMA:.2f}") # Formatted