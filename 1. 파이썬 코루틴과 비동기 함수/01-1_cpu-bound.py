# 프로그램이 실행될 떄 실행 속도가 CPU 속도에 의해 제한됨을 의미
# 복잡한 수학 수식을 계산하는 경우에 컴퓨터의 실행속도가 느려짐
def cpu_bound_func(number: int):
    total = 1
    arrange = range(1, number + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k

    return total


if __name__ == "__main__":
    result = cpu_bound_func(30)
    print(result)
