#encrypt and decrypt a text using a simple algorithm of offsetting the letters

key= 'abcdefghijklmnopqrstuvwxyz'

#function to encrypt the string and return the ciphertext
def encrypt (n, plaintext):
    result=''

    for l in plaintext.lower():
        try:
            i=(key.index(l) + n)
26
            result+=key[i]
        except ValueError:
            result += l

        return result.lower()

#function to decrypt the ciphertext and return the plain text

def decrypt(n, ciphertext)
    result=''

    for l in ciphertext:
        try:
            i =(key.index(l)-n)%
26
            result +=key[i]
        except ValueError:
            result += l
        return result

text = input(Enter the string:")
offset = int(input("enter the key:"))

encrypted= encrypt(offset, text)
             print('The plain text after encryption is:', encrypted)

decrypted = decrypt(offset, encrypted)
print('The cipher text after decryption is:', decrypted)
