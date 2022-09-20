import requests
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


# 17.5초 소요
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
