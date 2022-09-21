import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session, url = params[0], params[1]
    # os.getpid(): 현재 프로세스 id를 리턴
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    executor = ThreadPoolExecutor(
        max_workers=10
    )  # max_workers: 최대 스레드를 실행할 개수(==1: 싱글 스레드, >=2: 멀티 스레드)

    with requests.Session() as session:
        params = zip([session] * len(urls), urls)
        results = list(executor.map(fetcher, params))
        print(results)


# 8.4초 소요
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
