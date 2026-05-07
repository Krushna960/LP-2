# Assignment No. 1

s = "Hello\nWorld"

print("Original String:")
print(s)


# AND Operation
and_result = ""

for ch in s:
    and_result += chr(ord(ch) & 127)

print("\nAfter AND with 127:")
print(and_result)


# XOR Operation
xor_result = ""

for ch in s:
    xor_result += chr(ord(ch) ^ 127)

print("\nAfter XOR with 127:")
print(xor_result)