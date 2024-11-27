import multiprocessing

def get_square(n):
  return n * n

if __name__ == '__main__':
  numbers = [1,2,5,7,29]

  with multiprocessing.Pool() as pool:
    results = pool.map(get_square , numbers) 

    print(results)