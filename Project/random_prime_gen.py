import numpy as np
import math 

def prime_gen():
    while True:
        num = np.random.randint(1000,10000)
        prime = math.pow(num,50)
        prime_flag = 0
        if prime % 2 != 0:
            for i in range(2, int(math.sqrt(prime)) + 1):
                if (prime % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return prime
