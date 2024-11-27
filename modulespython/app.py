from reports import generate_expenses, generate_sales 
import asyncio

asyncio.run(generate_sales('Mayo'))
asyncio.run(generate_expenses('Mayo'))