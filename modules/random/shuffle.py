# Shuffles an list
import random

list = [1, 2, 3, 4, 5] # same list for sample.py

# before shuffle
print("Before shuffling the list:")
print(list) # prints the unshuffled list

random.shuffle(list) # shuffles the list
print("After shuffling the list")
print(list) # prints the shuffled list