"""
    These 2 methods will output cryptographically secure random real number in python given the input range.
"""

import os
import math
import secrets
import keys


def rnum_keygen_s(smallest, n):
    """The secrets module is only available in python 3.6 and above.
    This module is based on os.urandom() and random.SystemRandom()

    Args:
        smallest ([integer]): [this value depicts the min range for random generation]
        n ([integer]): [this value is used as the range from 0 to n to find the random number]

    Returns:
        [integer]: [returns a random integer within given range]
    """
    # instantiate systemRandom class instance from secrets module
    keyNumGen = secrets.SystemRandom()
    # generate cryptographically secure real number within range
    random_number = keyNumGen.randint(smallest, n)
    return random_number


def rnum_keygen_o(smallest, n):
    """[this method utilizes os.urandom and its quality of randomness is dependent on the operating system.
            - Windows internally utilizes CryptGenRandom()
            - Linux 3.17 and newer utilizes getrandom() syscall when available.
                - On OpenBSD 5.6 and newer, C's getentropy() is utilized.
            - UNIX utilizes /dev/urandom]

    Args:
        smallest ([integer]): [this value depicts the min range for random generation]
        n ([integer]): [this value is used as the range from 0 to n to find the random number]

    Returns:
        [integer]: [returns a random integer within given range]
    """
    # using log in base 2 of n to calculate total number of bit in n in log(n) time.
    bits = int((math.log(n) / math.log(2)) + 1)
    # using bits to find number of bytes within bits
    bitBytes = math.ceil(bits / 8)
    # to make sure the value is within range since os.urandom does not allow for range.
    random_number = 0
    while random_number < smallest:
        # random integer using os.urandom()
        random_number = int.from_bytes(os.urandom(bitBytes), byteorder="big")
    return random_number


# print('random key from secrets module: ', rnum_keygen_s(1, keys.g))
# print('random key from os and struct module: ', rnum_keygen_o(1, keys.g))
