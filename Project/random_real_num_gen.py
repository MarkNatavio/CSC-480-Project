"""
    These 2 methods will output cryptographically secure random real number in python given the input range.
"""

import os
import math
import secrets
import keys


def rnum_keygen_s(n):
    """The secrets module is only available in python 3.6 and above.
    This module is based on os.urandom() and random.SystemRandom()

    Args:
        n ([integer]): [this value is used as the range from 0 to n to find the random number]
    """
    # instantiate systemRandom class instance from secrets module
    keyNumGen = secrets.SystemRandom()
    # generate cryptographically secure real number within range
    random_number = keyNumGen.randint(0, n)
    return random_number


def rnum_keygen_o(n):
    """[
        this method utilizes os.urandom and its quality of randomness is dependent on the operating system.
            - Windows internally utilizes CryptGenRandom()
            - Linux 3.17 and newer utilizes getrandom() syscall when available.
                - On OpenBSD 5.6 and newer, C's getentropy() is utilized.
            - UNIX utilizes /dev/urandom

    Args:
        n ([integer]): [this value is used as the range from 0 to n to find the random number]
    """

    # using log in base 2 of n to calculate total number of bit in n in log(n) time.
    bits = int((math.log(n) / math.log(2)) + 1)
    # using bits to find number of bytes within bits
    bitBytes = math.ceil(bits / 8)
    # random integer using os.urandom()
    random_number = int.from_bytes(os.urandom(bitBytes), byteorder="big")
    return random_number


# print('random key from secrets module: ', rnum_keygen_s(keys.g))
# print('random key from os and struct module: ', rnum_keygen_o(keys.g))
