import csv 

# JUST READ EXAMPLES

file_path = './files/products.csv'

def simple_read(filename):
  with open(filename, mode='r') as products:
    csv_reader = csv.reader(products);
    for line in csv_reader: 
      print(line)

def dicc_read(filename):
  with open(filename, mode='r') as products:
    reader = csv.DictReader(products)
    for line in reader:
     print(line)

# APPEND A NEW LINE 

def dicc_add(filename):
  with open(filename, mode='a', newline='') as products:
    new_product = {
      'name': 'Chocorramo',
      'price': '500',
      'quantity': '123',
      'brand': 'Ramo',
      'category': 'Food',
      'entry_date': 'Hoy'
    }
    products.write('\n')
    writer = csv.DictWriter(products, fieldnames=new_product.keys())
    writer.writerow(new_product)


## CREATE AN UPDATING FILE 

updated_path = './files/updated_products.csv'

def updated_csv(filename, update_file_path):
  with open(filename, mode='r') as products:
    reader = csv.DictReader(products)
    new_field_names = reader.fieldnames + ['total']

    with open(update_file_path, mode='w', newline='') as updated:
      writer = csv.DictWriter(updated, new_field_names)
      writer.writeheader()

      for row in reader:
        row['total'] = float(row['price']) * int(row['quantity'])
        writer.writerow(row)
