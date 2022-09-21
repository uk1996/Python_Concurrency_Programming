import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor

nums = [30] * 100


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


# 23.4초(멀티 스레드를 하지 않은 코드랑 차이가 없다.)
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
