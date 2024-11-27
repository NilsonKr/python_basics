with open('./files/read.txt', 'r') as file:
  for lines in file:
    print(lines.strip())

with open('./files/read.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    print(line.strip())

with open('./files/read.txt', 'a') as file:
  file.write('\nHola tengo mucho suenito :c')

with open('./files/read.txt', 'w') as file: 
  file.writelines(iter(['Hola como estan', '\n\nteno sueno', ':c']))


##Count lines

with open('./files/read.txt', 'r') as file: 
  lines = file.readlines()
  print(f'Tiene {len(lines)} lineas')