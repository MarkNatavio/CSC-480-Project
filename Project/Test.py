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
    msg="Hello, this is Elgamal Encryption 2021"
    #p=random_prime_gen.prime_gen() #use prime_gen() to get prime number for Alice and bob
    p=313 #example

    print("prime number: ",p)
    #g=keys.g 
    g=151 #example

    #Alice_sk=random_real_num_gen.rnum_keygen_s(2,p-2)# get Alice's secret key randomly from 2 to p-2
    #Alice_pk=pow(g,Alice_sk,p) #get the Alice's public key
    Alice_sk=178 #exapmle
    Alice_pk=36 #example
    print("Alice:(secret key, public key) = ","(",Alice_sk,",",Alice_pk,")")
    
    #Bob_sk=random_real_num_gen.rnum_keygen_s(2,p-2)# get Bob's secret key randomly from 2 to p-2
    #Bob_pk=pow(g,Bob_sk,p) #get the Bob's public key
    Bob_sk=160 #example
    Bob_pk=113  #example
    print("Bob:(secret key, public key) = ","(",Bob_sk,",",Bob_pk,")")

    print("Alice gonna send the meassge : ", msg,"to Bob")

    Alice_enc=encryption.normal_version_enc(g,p,Alice_sk,msg,Bob_pk)# Alice gonna encryp the msg by using her secret key and Bob's public key
    print("Encrypted meassage: ", Alice_enc)

    c1=Alice_enc[0]
    c2=Alice_enc[1]
    Bob_dec=decryption.normal_version_elgamal_dec(c1,c2,p,Bob_sk) #Bob gonn decry the encrypted msg by using his secret key.
    
    Bob_dec = ''.join(Bob_dec)

    print("Bob decrypted the cipertext from Alice and got the plaintext:  ",Bob_dec)
    


normal_version_main()


'''
We run an example case here. If you want to use different secret key and public, you need to enable the command lines above #example.
p=313   g=151
-Bob(secret key, public key)=(160, 151^160 mod 313)= (160, 113)
-Alice(secret key, public key)=(178, 151^178 mod 313) = (178, 36)


'''
