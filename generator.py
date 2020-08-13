# a generator functions allow us to write a function that
# can send back a value and then later resume to pick up
# where it left off

#Allow us to generate a sequence of values over time

# when a generator function is compiled they become an object that supports
# an iteration protocol

# When they are called in code they don't actually return a value and then exit

#Will automatically suspend and resume their execution and state around the last point
# of value generation

# the advantage is that instead of having to compute an entire series
# of values up front, the generator computes one value waits
# until the next value is called for 

import random

def create_cubes(n):
  result = []
  for x in range(n):
    result.append(x**3)
  return result

def create_cubes_generator(n):
  for x in range(n):
    yield x**3

def gen_fibon(n):
  a = 1
  b = 1
  for i in range(n):
    yield a
    a,b = b, a+b


def simple_gen():
  for x in range(3):
    yield x

g = simple_gen()

print(next(g))

print(next(g))

# STOP iteration error says there is no more to yield


s = 'hello'
s_iter = iter(s)
next(s_iter)



def gensquares(N):
  for x in range(N):
    yield x**2

for num in gensquares(10):
  print(num)


def rand_num(low, high, n):
  for x in range(n):
    yield random.randint(low, high)

for num in rand_num(1,10,12):
  print(num)


# GENERATOR COMPREHENSION

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
  print(item)