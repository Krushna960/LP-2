# Assignment No. 5
# RSA Algorithm (Simple Version)


# Step 1: Choose two prime numbers
p = 3
q = 11


# Step 2: Calculate n and phi
n = p * q

phi = (p - 1) * (q - 1)


# Step 3: Choose e (Public Key)
e = 7


# Step 4: Find d (Private Key)
# d * e % phi = 1

for i in range(1, phi):

    if (i * e) % phi == 1:
        d = i
        break


# Display Keys
print("Public Key (e, n):", (e, n))

print("Private Key (d, n):", (d, n))


# Message
msg = 9

print("Original Message:", msg)


# Encryption
# c = (msg ^ e) % n

c = (msg ** e) % n

print("Encrypted Message:", c)


# Decryption
# m = (c ^ d) % n

m = (c ** d) % n

print("Decrypted Message:", m)