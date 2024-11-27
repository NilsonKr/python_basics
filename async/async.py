import asyncio


async def download(file: str):
  print('Descarga iniciada')

  await asyncio.sleep(10)

  print('Descarga finalizada')

async def main():
  file = input('ingrese el nombre del archivo')
  
  await download(file)

  print(f'Archivo {file} descargado con exito')


asyncio.run(main())