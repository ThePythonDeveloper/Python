# simliar to choice.py
import random

K = 14 # replace with your K here
LIST = ["apple", "banana", "cherry"]
CHOOSE = random.choices(LIST, weights= [10,1,1], k=K)

# OUTPUT
print(CHOOSE)