## CONVERT A CSV FILE INTO JSON AND BACKWARDS

import csv 
import json

def csv_to_json(path, new_path): 
  with open(path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    with open(new_path, mode='w', newline='') as json_file:
      json.dump(list(csv_reader), json_file, indent=4)

# csv_to_json('./files/converter/cats_data.csv', './files/converter/cats_data.json')


def json_to_csv(path, new_path):
  with open(path, mode='r') as file:
    reader = json.load(file)
    fieldnames = reader[0].keys()

    with open(new_path, mode='w', newline='') as new_file:
      writer = csv.DictWriter(new_file, fieldnames)
      writer.writeheader()
      writer.writerows(reader)

json_to_csv('./files/converter/coffee.json', './files/converter/coffee.csv')