# restore the state of the random number generator
import random


RANDOM_NUMBER = random.random() # prints a random num
STATE = random.getstate() # gets the current state
ANOTHER_RANDOM_NUMBER = random.random() # another one
ANOTHER_ONE = random.random()

# outputs
print(f"Random number: {RANDOM_NUMBER}") # output 1
print(f"Another random number: {ANOTHER_RANDOM_NUMBER}")
random.setstate(STATE) # restoes the state
print(f"Another random number, again;: {ANOTHER_ONE}")