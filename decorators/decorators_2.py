import os 
from enum import Enum
from typing import TypedDict


class TypedEmployee(TypedDict):
  name: str
  role: str


class EnumRoles(Enum):
  user = 'User'
  admin = 'Admin'


def check_role(role: EnumRoles):
  def decorator(func): 
    def wrapper(employee: TypedEmployee, order_id: int):
      if employee['role'] == role:
        func(employee, order_id)
      else:
        print('No tiene permitido esta accion')
    return wrapper

  return decorator

def log_action(action: str):
  def decorator(func):
    def wrapper(employee: TypedEmployee, order_id: int):
      func(employee, order_id)

      cwd = os.getcwd()
      with open(f'{cwd}/decorators/logs.txt', mode='a', newline='' ) as file:
        file.write(f'{employee['name']} has {action} order#{order_id}' + '\n')

    return wrapper
  
  return decorator


@check_role(EnumRoles.admin)
@log_action('update')
def update_order(employee: TypedEmployee, order_id: int):
  print(f'{employee['name']} has update order#{order_id}')

nilson = {'name': 'Nilson', 'role': EnumRoles.user}
nico = {'name': 'Nico', 'role': EnumRoles.admin}

update_order(nilson, 2313)
update_order(nico, 2313)

