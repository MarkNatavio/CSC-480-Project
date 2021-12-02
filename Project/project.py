import random

def enc(g, p, key, m, pk): # El Gamal Encryption Scheme
  '''
  Inputs:
  g - some integer
  p - prime number
  key - public key
  m - message
  pk - private key (comes from decryption algorithm)
  
  Outputs:
  c1, c2 - Encrypted messages
  '''
  c1 = pow(g,key,p)
  
  g2 = pow(g,pk,p)
  c2 = (m*(pow(g2,key)))%p
  return c1, c2
