import os
import math
import secrets
import keys
from random_real_num_gen import rnum_keygen_o
import encryption
import decryption
import keys
import random_prime_gen
import random_real_num_gen

def normal_version_main():
    msg="2345678901234567890123456789012345678901234567890123"
    p=random_prime_gen.prime_gen() #use prime_gen() to get prime number for Alice and bob

    print("prime number: ",p)
    g=keys.g 

    Alice_sk=random_real_num_gen.rnum_keygen_s(2,p-2)# get Alice's secret key randomly from 2 to p-2
    Alice_pk=pow(g,Alice_sk,p) #get the Alice's public key
    print("Alice:(secret key, public key) = ","(",Alice_sk,",",Alice_pk,")")
    
    Bob_sk=random_real_num_gen.rnum_keygen_s(2,p-2)# get Bob's secret key randomly from 2 to p-2
    Bob_pk=pow(g,Bob_sk,p) #get the Bob's public key
    print("Bob:(secret key, public key) = ","(",Bob_sk,",",Bob_pk,")")

    print("Alice gonna send the meassge : ", msg,"to Bob")

    Alice_enc=encryption.normal_version_enc(g,p,Alice_sk,msg,Bob_pk)# Alice gonna encryp the msg by using her secret key and Bob's public key
    print("Encrypted meassage: ", Alice_enc)

    c1=Alice_enc[0]
    c2=Alice_enc[1]
    Bob_dec=decryption.normal_version_elgamal_dec(c1,c2,p,Bob_sk) #Bob gonn decry the encrypted msg by using his secret key.
    print("Bob decrypted the cipertext from Alice and got the plaintext:  ",Bob_dec)
    


normal_version_main()
