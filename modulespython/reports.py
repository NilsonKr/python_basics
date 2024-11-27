import asyncio

async def generate_sales (month:str):
  print('Generando reporte de ventas')
  await asyncio.sleep(2)
  print(f'Reporte de ventas para el mes de {month} generado')

async def generate_expenses (month:str):
  print('Generando reporte de gastos')
  await asyncio.sleep(1)
  print(f'Reporte de gastos para el mes de {month} generado')
