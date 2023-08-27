# Generates a random number thats the same based of the seed
import random

SEED = 42 # set the seed to whatever, we are using a number for this example
START_RANGE = 1
END_RANGE = 100

random.seed(SEED)
number = random.randint(START_RANGE, END_RANGE)
print(number) # it prints the same number no matter what aslong as the seed is the same
# so it printed out 82 for me, and when i ran it again same result, so this is based of the seed