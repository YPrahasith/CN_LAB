# 5. Write a program for simple RSA algorithm to encrypt and decrypt the data.

from Crypto.Util import number

def gen_keys():

    bit_length = 256

    p = number.getPrime(bit_length)
    while True:
        q = number.getPrime(bit_length)
        if p != q:
            break

    N = p * q
    ctf = (p-1) * (q-1)

    while True:
        e = number.getPrime(8)
        if ctf % e != 0:
            break

    d = number.inverse(e, ctf)

    return (e, N), (d, N)

def encrypt(plaintext, public_key):

    num = int(plaintext)

    enc = pow(num, public_key[0], public_key[1])

    return enc

def decrypt(ciphertext, private_key):
    
    cipher = int(ciphertext)

    dec = pow(cipher, private_key[0], private_key[1])

    return dec

if __name__ == '__main__':
    
    public_key, private_key = gen_keys()


    while True:
        print()
        print('1. Encrypt\n2. Decrypt\n3. Exit')
        choice = int(input())

        if choice == 1:
            plaintext = input('Enter text to be encrypted: ')
            print("Encrypted = ", encrypt(plaintext, public_key))

        elif choice == 2:
            ciphertext = input('Enter text to be decrypted: ')
            print("Decrypted = ", decrypt(ciphertext, private_key))

        else:
            break