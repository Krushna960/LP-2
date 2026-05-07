# Assignment No. 4
# AES Algorithm (Simplified using XOR Logic)


def encrypt(text, key):

    result = ""

    for i in range(len(text)):

        # XOR text character with key character
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return result


def decrypt(cipher, key):

    result = ""

    for i in range(len(cipher)):

        # XOR again with same key
        result += chr(ord(cipher[i]) ^ ord(key[i % len(key)]))

    return result


# Main Program
text = "HELLO"
key = "SECRET"

print("Original Text:", text)
print("Key:", key)


# Encryption
enc = encrypt(text, key)

print("Encrypted:", [ord(c) for c in enc])


# Decryption
dec = decrypt(enc, key)

print("Decrypted:", dec)