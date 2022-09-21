import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor

nums = [30] * 100

# cpu 집약적인 연산을 할때는 멀티 스레딩보다 멀티 프로세싱이 효율적이다.
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
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


# 13.5초 소요
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
