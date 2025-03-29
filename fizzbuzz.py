def fizzbuzz(value):
    if value % 15 == 0:
        return "fizzbuzz"
    elif value % 3 == 0:
        return "fizz"
    elif value % 5 == 0:
        return "buzz"

    return str(value)


if __name__ == "__main__":
    for number in range(1, 101):
        print(fizzbuzz(number))
