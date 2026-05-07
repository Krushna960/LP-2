# Simple DES-like Encryption using XOR


def encrypt(text, key):

    result = ""

    for i in range(len(text)):

        # XOR text character with key character
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return result


def decrypt(cipher, key):

    result = ""

    for i in range(len(cipher)):

        # XOR again to get original text
        result += chr(ord(cipher[i]) ^ ord(key[i % len(key)]))

    return result


# Main Program
text = "HELLO"
key = "KEY"

enc = encrypt(text, key)

print("Encrypted:", [ord(c) for c in enc])

dec = decrypt(enc, key)

print("Decrypted:", dec)