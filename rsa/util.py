def is_prime(n):
    """
    Time complexity O(sqrt(n)).
    :param n: number to check.
    :return: true if n is a prime number else false.
    """
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def euler_func(p, q):
    """
    Calculates the Euler function value for two given prime numbers, p and q, using the formula: (p - 1) * (q - 1)
    :param p: the first prime number.
    :param q: the second prime number.
    :return: result of Euler function.
    """
    return (p - 1) * (q - 1)


def extended_euclidean_algorithm(a, b):
    """
    Implements the Extended Euclidean algorithm to find the greatest common divisor (gcd) of two numbers, a and b,
    and also calculates the values of x and y satisfying the equation ax + by = gcd(a, b).
    :param a: the first number.
    :param b: the second number.
    :return: tuple (gcd, x, y) containing the gcd of a and b, and the values x and y.
    """
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def modular_inverse(num, mod):
    """
    Calculates the modular inverse of a number num with respect to a modulus mod using the Extended Euclidean algorithm.
    :param num: the number for which the modular inverse is to be calculated.
    :param mod: the modulus value.
    :return: modular inverse of num modulo mod.
    """
    return extended_euclidean_algorithm(num, mod)[1] % mod
