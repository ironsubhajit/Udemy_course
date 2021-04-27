import time
from threading import Thread


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

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
# start the thread to execute
thread1.start()
thread2.start()

thread1.join() # tells main thread to wait for thread1 to finish
thread2.join() # tells main thread to wait for thread2 to finish

print(f'Two thread total time, {time.time() - start}')
