def is_prime(n):
    if (n == 1):
        return False
    if (n == 2):
        return True
    if n % 2 == 0:
        return False

    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


print(is_prime(13))
