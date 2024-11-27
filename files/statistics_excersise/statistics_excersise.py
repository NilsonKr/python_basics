import statistics
import csv

def get_sales_statistics(): 
  with open('./files/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)

    sales = []
    for row in reader:
      sales.append(int(row['sales']))

    print(f'''
Media: {statistics.mean(sales)}
Mediana: {statistics.median(sales)}
Median: {statistics.median(sales)}
Desviacion Estandar: {statistics.stdev(sales)}
Varianza: {statistics.variance(sales)}

''')
    
get_sales_statistics()
    
