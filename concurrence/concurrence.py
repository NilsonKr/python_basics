import threading

balance = 0
lock = threading.Lock()

def deposit_balance(amount: int):
  global balance
  for _ in range(1000):
    with lock:
      balance += amount


threads : list[threading.Thread] = []

for _ in range(3):
  thread = threading.Thread(target=deposit_balance, args=(1,))
  threads.append(thread)
  thread.start() 

for thread in threads:
  thread.join()


print(f'Balance: ${balance}')