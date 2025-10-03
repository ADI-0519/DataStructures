# Prefix sums - Helpful when playing around with subarray sums + Kadane's Algo (Greedy approach)
# Some questions may require you to go from left to right or right to left
# Some questions also require use of two pointers or sliding window (variable or fixed size)

A = ["mass","as","hero","superhero"]
S =  "   fly me   to   the moon  "
B = [1, 3, 4, 6, 1, 9, 10]
c = "c"
string = "hello"

# for i in range(len(string)):
#     if i == 1:
#         string[i] = "b"

# print(string)


print(max(B), min(B))
print(sum(B))

# .strip() used to remove leading and trailing whitespaces ONLY.

print(S.strip())

# .join() used to join an array into a string.
# sep.join(iterable)

s = " ".join(A)
print(s)

# .split() used to split a string into array items using a dilimeter

print(s.split(" "))

# s.lower() and s.upper() for capitalising and lowering.

# ord(c) and chr(c)

print(ord(c))
print(chr)

# .count() return snumber of non overlapping occurences of a substring useful for subsequences.

print("banana".count("an"))


# Prefix sum part:

def prefix(arr):
    n = len(arr)
    pref = [0] * (n+1)

    for i in range(1, n+1):
        pref[i] = pref[i-1] + arr[i-1]

    return pref

print(prefix(B))

# Sum between i,j indices is pref[j+1] - pref[i]

def prefix_alt(arr):
    n = len(arr)
    pref = [0] * n
    total = 0

    for i in range(n):
        total += arr[i]
        pref[i] = total

    return pref

print(prefix_alt(B))

# Sum between i,j inclusive: pref[j] - pref[i-1]