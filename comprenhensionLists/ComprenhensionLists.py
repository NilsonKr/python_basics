# Squares numbers 

squares = [x**2 for x in range(1,11)]

print('Squares', squares)

# Celsius to Farenheit ((x * 9/5) + 32)

celsius = [9, 11, 21, 30, 34]
farenheit = [(f * 9/5) + 32 for f in celsius]

print(farenheit)

# Evens & Odss

evens = [even for even in range(1,21) if even % 2 == 0]
odds = [odd for odd in range(1,21) if odd % 2 != 0]

print(evens, odds)


# Transposed Matrix

base_matrix = [[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12],]


transposed_matrix = [[row[i] for row in base_matrix] for i in range(len(base_matrix[0]))]


print(transposed_matrix)
# print(range(len(base_matrix[0])))

## Normal transposed list 

normal_transposed = []


for index in range(len(base_matrix[0])):
  new_row = []
  for row in base_matrix:
    new_row.append(row[index])
  normal_transposed.append(new_row)


print(normal_transposed, 'normal')