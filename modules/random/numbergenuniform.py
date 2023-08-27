# Generates a random number
import random

START_RANGE = 1
END_RANGE = 100

gen = random.uniform(START_RANGE, END_RANGE) # intalizes the main randomn number generator
# looks like 3.18
print(gen) # NO FORMAT
print(f"{gen:.2f}") # FORMAT