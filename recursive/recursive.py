# Factorial in a recursive way

def calc_factorial(number): 
  if number == 0:
    return 1

  return number * calc_factorial(number -1)


print(calc_factorial(5))  

# fibonacci

def recursive_fibonacci(n): 
  if n == 0: return 0
  if n == 1: return 1

  return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

print(recursive_fibonacci(20))


## See error exception herarchy

def print_exception_subclasses(exception, indent = 0):
  print(' ' * indent, exception.__name__)
  for subclass in exception.__subclasses__():
    print_exception_subclasses(subclass, indent + 4)

print_exception_subclasses(Exception)