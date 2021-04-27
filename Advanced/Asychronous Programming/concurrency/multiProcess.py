import time
from multiprocessing import Process


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


if __name__ == '__main__':
    start1 = time.time()
    ask_user()
    complex_calculation()
    print(f'Single Thread total time, {time.time() - start1}')

    start = time.time()
    process = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)

    process.start()
    process2.start()

    process.join()
    process2.join()

    print(f'Two thread total time, {time.time() - start}')
