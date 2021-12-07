from random_real_num_gen import rnum_keygen_o
import keys


def prime_gen():
    prime = rnum_keygen_o(1, keys.MAX_NUM_2048, 0)
    op = True
    if prime == 0 or prime == 1:
        op = False
    while True:
        if op == False:
            prime += 1
        else:
            prime -= 1
        prime_flag = 0
        if prime % 2 != 0:
            for i in range(2, prime // 2):
                if (prime % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return prime
