def get_prime_factors(number):
    candidates = [2]
    candidates.extend(range(3, number + 1, 2))

    result = []
    for candidate in candidates:
        while number % candidate == 0:
            number = number / candidate
            result.append(candidate)

            if number == 1:
                return result

    return [number]
