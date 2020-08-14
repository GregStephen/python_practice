import math

value = 4.35

math.floor(value) 
# 4

math.ceil(value)
# 5

round(4.35)
# will be 4

# round will if 4.5 will go to 4,
# 5.5 will go to 6 though because
# it chooses all evens when split


# setting a seed makes the same random numbers show up
import random
# returns some random integer
random.randint(0,100)
random.seed(42)

mylist = list(range(0, 20))

random.choice(mylist)


# sample with replacement, integer can be picked more than once

random.choices(population=mylist, k=10)

# sample without replacement, once you pick a number, cant pick again

random.sample(population=mylist, k=10)


random.shuffle(mylist) # permanently affects it in place

