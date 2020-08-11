def func():
  return 1

def hello():
  return "Hello!"

greet = hello

greet()

def hey(name = 'Greg'):
  print('The hey() function has been executed!')

  def greet():
    return '\t this is the greet() func inside hello!'

  def welcome():
    return '\t this is the welcome() inside hello'

  print('I am going to return a function!')

  if name == 'Greg':
    return greet
  else:
    return welcome

my_new_func = hey('Greg')
print(my_new_func())

def cool():
  
  def super_cool():
    return 'I am very cool!'

  return super_cool

some_func = cool()

print(some_func())

def other(some_def_func):
  print('Other code runs here!')
  print(some_def_func())

other(hello)


def new_decorator(original_func):

  def wrap_func():
    print('Some extra code, before the original function')

    original_func()

    print('Some extra code, after the original function')

  return wrap_func

def func_needs_deecorator():
  print('I want to be decorated!')

decorated_func = new_decorator(func_needs_deecorator)

decorated_func()

@new_decorator
def func_needs_decorator():
  print('I want to be decorated!')

func_needs_decorator()