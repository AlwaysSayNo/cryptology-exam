import random
from util import is_prime, euler_func, extended_euclidean_algorithm, modular_inverse


def rsa_encrypt(public_key, plain_text):
    """
    Encrypt text using input parameters.
    :param public_key: generated public key (e, n).
    :param plain_text: user's text.
    :return: encrypted with public key (e, n) user's text.
    """
    e, n = public_key
    return [pow(ord(char), e, n) for char in plain_text]


def rsa_decrypt(private_key, encrypted_text):
    """
    Decrypt text using input parameters.
    :param private_key: generated private key (d, n).
    :param encrypted_text: encrypted user's text.
    :return: decrypted with private key (d, n) user's text.
    """
    d, n = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in encrypted_text]
    return ''.join(decrypted_text)


def generate_keys(bit_length):
    """
    Function is responsible for generating the public and private keys required for the RSA algorithm.
    :param bit_length: an integer representing the desired length of the keys in bits.
    :return: tuple (public_key, private_key) containing the generated public key (e, n) and private key (d, n).
    """
    half_bit_length = bit_length // 2
    while True:
        p = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
        if is_prime(p):
            break
    while True:
        q = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
        if is_prime(q) and p != q:
            break
    # Calculation of the module
    n = p * q
    # Public key creation
    phi = euler_func(p, q)
    while True:
        e = random.randint(3, phi - 1)
        if extended_euclidean_algorithm(e, phi)[0] == 1:
            break
    pub_key = (e, n)
    # Private key creation
    d = modular_inverse(e, phi)
    priv_key = (d, n)

    return pub_key, priv_key
