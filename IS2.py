# Assignment No. 2

def encrypt(text, key):

    # Create empty rows
    res = [""] * key

    row = 0
    step = 1

    # Place characters in zig-zag pattern
    for ch in text:

        res[row] += ch

        # Change direction
        if row == 0:
            step = 1

        elif row == key - 1:
            step = -1

        row += step

    return "".join(res)


def decrypt(cipher, key):

    n = len(cipher)

    # Store zig-zag row pattern
    pattern = [0] * n

    row = 0
    step = 1

    # Generate pattern
    for i in range(n):

        pattern[i] = row

        if row == 0:
            step = 1

        elif row == key - 1:
            step = -1

        row += step

    # Empty result array
    res = [""] * n

    index = 0

    # Fill characters row by row
    for r in range(key):

        for i in range(n):

            if pattern[i] == r:
                res[i] = cipher[index]
                index += 1

    return "".join(res)


# Main Program
text = input("Enter text: ")
key = int(input("Enter key: "))

c = encrypt(text, key)

print("Encrypted:", c)
print("Decrypted:", decrypt(c, key))