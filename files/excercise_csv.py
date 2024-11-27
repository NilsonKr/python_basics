## CREATE AN UPDATING FILE WITH TOTAL SALES THROUGH MONTHS AND DISPLAY THEM
import csv

file_path = './files/monthly_sales.csv'
updated_path = './files/monthly_sales_total.csv'

def read_csv(path):
 with open(path, mode='r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    print(row)

def write_total(path, updated_path):
  with open(path, mode='r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['total']

    with open(updated_path, mode='w', newline='') as updated:
      writer = csv.DictWriter(updated, fieldnames)
      writer.writeheader()
      last_total = 0

      for row in reader:
        last_total += int(row['sales'])
        row['total'] = last_total
        writer.writerow(row)

  read_csv(updated_path)



write_total(file_path, updated_path)