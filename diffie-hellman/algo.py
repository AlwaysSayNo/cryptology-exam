from util import enter_public_number, enter_private_key


def calc_public_values(g, p, x1, x2):
    """
    Calculates public values by formulas: user_1_pv = (g^x_1)mod(p), (g^x_2)mod(p)
    :param g: public key P
    :param p: public key G
    :param x1: user_1 private private key
    :param x2: user_2 private private key
    :return: public values of user_1, user_2
    """
    return pow(g, x1) % p, pow(g, x2) % p


def cal_secret_keys(p, x1, x2, y1, y2):
    """
    Calculates public values by formulas: user_1_pv = (y_2^x_1)mod(p), (u_1^x_2)mod(p)
    :param p: public key P
    :param x1: user_1 private private key
    :param x2: user_2 private private key
    :param y1: user_1 private public value
    :param y2: user_2 private public value
    :return: public values of user_1, user_2
    """
    return pow(y2, x1) % p, pow(y1, x2) % p


def diffie_hellman():
    P = enter_public_number("-> Enter public number (prime) P: ")
    G = enter_public_number("-> Enter public number (prime) G: ")

    x1 = enter_private_key(f"-> User_1 enters number (less then {P}): ", P)
    x2 = enter_private_key(f"-> User_2 enters number (less then {G}): ", G)

    y1, y2 = calc_public_values(G, P, x1, x2)
    secret_1, secret_2 = cal_secret_keys(P, x1, x2, y1, y2)

    return [secret_1, secret_2]
