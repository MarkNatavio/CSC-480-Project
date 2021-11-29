# CSC-480-Project

# El-Gamal Encyption Scheme (plain)

- Key Gen:

  - Generate random number, a large prime, p
  - g should be a random from {2,...,p-1}
  - Secret key:
    - generate secret key, random k from {2,...,p-2}
  - Public key:
    - publish public key, pk, (g^k mod p). (g and p are public)

- Public:

  - g and p are public

- Encryption (pk, m):

  - message should be from {1,...,p-1}
  - pick random, r from {1,...,p-1}
  - Ciphertext:
    - C = {c1: g^r mod p, c2: m \* pk^r mod p}

- Decryption (sk, (c1,c2)):

  - m = ((c2) / (c1^k)) mod p
  - equivalent to...
    - (m \* (g^k mod p)^r mod p) / (g^r mod p)^k

- Example:

  - code:

  ```
    p = 61
    g = 14
    k = 16
    pk = (g ^ k) % p
    m = 50
    r = 41
    C = {'c1': (g ^ r) % p, 'c2': m \* ((pk ^ r) % p)}
    print("Encryption of", m, "is: ", C)
    dec_m = ((C['c2']) / (C['c1'] ^ k)) % p
    # dec_m = (m \* (((g ^ k % p) ^ r) % p)) / (((g ^ r) % p) ^ k)
    print("Deccryption of", C, "is: ", dec_m)
  ```

  - output:

  ```
    > > Encryption of 50 is: {'c1': 39, 'c2': 2750}
    > > Deccryption of {'c1': 39, 'c2': 2750} is: 50.0
  ```
