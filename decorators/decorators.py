from typing import TypedDict
import os

class TypedEmployee(TypedDict):
  name: str
  role: str


def log_employee_action(action_fn): 
  def wrapper(action: str):
    action_fn(action)

    cwd = os.getcwd()
    with open(f'{cwd}/decorators/logs.txt', mode='a', newline='' ) as file:
      file.write(action+'\n')

  return wrapper


@log_employee_action
def print_employee_action(action: str):
  print(action)
  

def employee_login(employee: TypedEmployee, ) -> None: 
  print_employee_action(f'{employee["name"]}, rol: {employee["role"]}, ingreso al sistema.')


def employee_logout(employee: TypedEmployee) -> None: 
  print_employee_action(f'{employee["name"]}, rol: {employee["role"]}, salio del sistema.')


nilson = {'name': 'Nilson', 'role': 'employee'}
nico = {'name': 'Nico', 'role': 'admin'}

employee_login(nilson)
employee_login(nico)
employee_logout(nico)
employee_logout(nilson)
