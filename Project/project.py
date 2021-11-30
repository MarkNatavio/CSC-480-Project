import random

def enc(g, p, key, m, pk): # El Gamal Encryption Scheme
  c1 = pow(g,key)%p
  
  g2 = pow(g,pk)%p
  c2 = m*(pow(g2,key)%p)
  return c1, c2
