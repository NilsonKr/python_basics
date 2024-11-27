import json

#Read files

file_path = './files/products.json'

def read_json(file_path):
  with open(file_path, mode='r') as file:
    products = json.load(file)

    for product in products:
      print(product)


## Apend new item

def append_product(file_path):
  with open(file_path, mode='r') as file:
    new_product = {
          'name': 'Chocorramo',
          'price': '500',
          'quantity': '123',
          'brand': 'Ramo',
          'category': 'Food',
          'entry_date': 'Hoy'
        }
    
    json_reader = json.load(file)
    json_reader['products'].append(new_product)

    with open(file_path, mode='w') as file:
      json.dump(json_reader, file, indent=4)


append_product(file_path)