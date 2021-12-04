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
