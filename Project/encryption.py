import random

def enc(g, p, pk, m, sk): # El Gamal Encryption Scheme
  '''
  Inputs:
  g - some integer
  p - prime number
  pk - public key
  m - message
  sk - secret key (comes from decryption algorithm)
  
  Outputs:
  c1, c2 - Encrypted messages
  '''
  c1 = pow(g,pk,p) # getting c1
  
  g2 = pow(g,sk,p) # encryption with private key
  c2 = (m*(pow(g2,pk)))%p # getting c2
  
  return c1, c2



#Alternate method
def normal_version_enc(g, p, ssk, m, rpk): # Normal version of El Gamal Encryption Scheme
  '''
  Inputs:
  g - some integer
  p - prime number
  ssk - sender's secret key
  m - message
  rpk- receiver's public key   =  g^(receiver's secret key) mod p
  Outputs:
  y1, y2 - Encrypted messages
  '''


  enc_m = []
  for i in range(0, len(m)):
        enc_m.append(m[i])
  
  for i in range(0, len(enc_m)):
        enc_m[i] = (ord(enc_m[i])*pow(rpk,ssk)) % p 

  y1 = pow(g,ssk,p) # getting c1
  y2= enc_m        # getting c2
 # y2 = (m*pow(rpk,ssk)) % p 
  
  return y1, y2


'''
Example of Alice sending meassge to Bob by using normal version of Elgamal encryption and decryption.
-prime number=37, g=2

-Bob(secret key, public key)=(5, 2^5 mod 37)= (5, 32)
-Alice(secret key, public key)=(7, 2^7 mod 37) = (7, 17)

-Shared secret keys:
-Alice: (Bob's public key)^(Alice's secret key) mod p= (17^5) % 37=19
-Bob:  (Alice's public key)^(Bob's secret key) mod p=(32^7) % 37 =19
-Thus, Alice and Bob use the same shared secret key.

-Alice wants to send msg 29 to Bob.
-Then she uses her secret key 7 to encrypt it.

-y1=g^(Alice's secret key) mod p= 2^7 mod 37= 17
-y2= msg *  (Bob's secret key)^(Alice's secret key) mod p= 29* 32^7 mod 37 = 33

-Bob receives (y1,y2)=(17,33) from Alice.

-msg=c2* ( c1^(Bob's secret key) ^(-1) mod p
       =33 *( 17 ^5) ^(-1) mod 37
       =29  (correct!!)


'''

