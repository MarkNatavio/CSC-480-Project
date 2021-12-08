def elgamal_dec(c1,c2,p,sk):

    """
    inputs
    c1: cipytertext c1
    c2: cipytertext c2
    p: prime number
    sk: secret key

    output
    dec_m: decrypted message
    """
    dec_m = pow(c1,(p-sk-1))*c2%p
    return dec_m

# test:
# c1 = 48, c2 = 40, p = 61, sk = 16
# elgamal_dec(48,40,61,16) = 50





#Alternate method
def normal_version_elgamal_dec(y1,y2,p,rsk):

    """
    inputs
    y1: cipytertext y1
    y2: cipytertext y2
    p: prime number
    rsk: receiver's secret key

    output
    dec_m: decrypted message
    """
    dec_m = pow(y1,(p-rsk-1))*y2%p
    return dec_m


