import multiprocessing

def get_square (numbers: list[int], que: multiprocessing.Queue):
  for n in numbers:
    que.put(n * n)

if __name__ == '__main__':
  numbers = [1,23,43,12]

  queue = multiprocessing.Queue()
  
  process = multiprocessing.Process(target=get_square, args=(numbers,queue) )

  process.start()
  process.join()

  while not queue.empty():
    print(queue.get())

