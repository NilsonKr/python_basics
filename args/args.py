calc_discount = lambda discount, value: int(value) - ((int(discount) / 100) * int(value))

def show_products(*args, **kwargs):
  products_list = map(lambda product: {'name': product['name'], 'value': calc_discount(kwargs['discount'], product['value']) if product['name'] in kwargs['on_sale'] else product['value'] },  list(args))
  print(list(products_list))

inventory = [
  {'name':'KitKat', 'value': 5000},
  {'name':'Chocorramo', 'value': 2000},
  {'name':'Trident', 'value': 1000},
  {'name':'SpeedMax', 'value': 2500},
  {'name':'Mani', 'value': 3800},
]

show_products(*inventory, on_sale=['Mani', 'KitKat'], discount=30)