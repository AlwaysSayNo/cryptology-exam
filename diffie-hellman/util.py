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


def enter_public_number(message):
    """
    Asks user to enter prime number.
    :param message: prompt message.
    :return: prime number x.
    """
    while True:
        x = int(input(message))
        if not is_prime(x):
            print(f"Number should be prime!")
            continue
        break

    return x


def enter_private_key(message, n):
    """
    Asks user to enter prime number.
    :param n: number to check.
    :param message: prompt message.
    :return: private key x.
    """
    while True:
        x = int(input(message))
        if x >= n:
            print(f"PK of user should be < {n}!")
            continue
        break

    return x
