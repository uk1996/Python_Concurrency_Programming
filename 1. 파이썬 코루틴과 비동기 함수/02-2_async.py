# 코드가 비동기적으로 동작한다 => 코드가 반드시 작성된 순서 그대로 실행되는 것이 아니다.

# 루틴: 일련의 명령(코드의 흐름)
#   - 메인 루틴: 프로그램의 메인 코드의 흐름
#   - 서브 루틴: 보통의 함수나 메소드(메인 루틴을 보조하는 역할) / 하나의 진입점과 하나의 탈출점이 있는 루틴
#   - 코루틴: 서브 루틴의 일반화된 형태 / 다양한 진입점과 다양한 탈출점이 있음

# 어웨이터블(awaitable) 객체: 코루틴, 태스크, 퓨처
#    - 태스크: 코루틴을 동시에 예약하는데 사용
#           - task1 = asyncio.create_task(delivery("A", 2)) # 태스크를 예약
#           - task2 = asyncio.create_task(delivery("B", 2)) # 태스크를 예약
#           - await task2 # 태스크를 실행
#           - await task1 # 태스크를 실행
#    - 퓨처: 저수준 어웨이터블 객체
import time
import asyncio

# 코루틴 함수
async def delivery(name, mealtime):  # 진입점 1
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)  # 탈출점 1 / 진입점 2
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime  # 탈출점 2


async def main():
    result = await asyncio.gather(
        delivery("A", 10), delivery("B", 3), delivery("C", 4)
    )  # 어웨이터블 객체를 동시에 실행

    print(result)


# 동기적으로 수행되기를 원할때
# async def main():
#     await delivery("A", 10)
#     await delivery("B", 3)
#     await delivery("C", 4)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())  # asyncio.run: 코루틴 함수를 싱행하고 결과를 반환
    end = time.time()
    print(end - start)
