def fibo(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1

    return fibo(value - 1) + fibo(value - 2)
