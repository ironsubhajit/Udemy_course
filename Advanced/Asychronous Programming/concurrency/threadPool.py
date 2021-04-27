import time
from concurrent.futures import ThreadPoolExecutor
# threadPoolExecutor are used now days for using Threads

def ask_user():
    start = time.time()
    user_input = input("enter your name: ")
    greet = f'hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')

def complex_calculation():
    start = time.time()
    print('start calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculating, {time.time() - start}')

start1 = time.time()
ask_user()
complex_calculation()
print(f'Single Thread total time, {time.time() - start1}')

start = time.time()
# start the thread to execute
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(ask_user)
    pool.submit(complex_calculation)


print(f'Two thread total time, {time.time() - start}')
