# Convert decimal to binary, removing the 0b part.
# returns a string version

print(bin(5)[2:])



binary = '101'
print(int(binary,2))


# Bitwise operations

print(5 & 7) # --> 5
print(5 | 7) # --> 7
print(5 ^ 7) # --> 2
print(~5) # --> -6
print(5 << 2) # --> Performs a arithmetic left shift
print(5 >> 1) # --> Performs a signed right shift

print(hex(5)) # --> '0x5'

# quick rules:
# n & n-1 removes the last set bit
# n & -n gives the last set bit
# n | n-1 sets all bits to the right of the last set bit
# n ^ -1 flips all bits
# n << 1 multiplies by 2
# n >> 1 divides by 2