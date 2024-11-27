# Evens & odds 

odds_iter  = iter(range(1, 11, 2))
evens_iter = iter(range(0, 11, 2))

 ##Fibonacci 

def fibonacci_gen (limit): 
  a, b = 0, 1
  while a <= limit: 
    yield a 
    a, b = b, a+b


for num in fibonacci_gen(13):
  print(num)

## Fibonnacci list

fib_list = []

a = 0
b = 1

for num in range(0, 8):
  fib_list.append(a)
  a, b = b,  a + b
   

print(fib_list)