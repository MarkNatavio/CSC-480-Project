
def dec(c1,c2,p,pk):               # El Gamal Decryption Scheme
  '''
  Inputs:
  c1, c2 - Encrypted messages
  p - prime number
  pk - private key (comes from decryption algorithm)
  
  Outputs:
  d - decrypted messages
  '''
  s=pow(c1,pk,p)   
  d = (c2/s)%p

  return d
  


