def fibo(number: int) -> int:
    if number <= 1:
        return number
    return number * fibo(number - 1)


print(fibo(7))
