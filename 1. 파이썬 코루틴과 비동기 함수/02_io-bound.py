# 프로그램이 실행될 때 실행 속도가 I/O에 의해 제한됨을 의미
def io_bound_func():
    print("value:")
    input_value = input()
    return int(input_value) + 100


if __name__ == "__main__":
    result = io_bound_func()
    print(result)
