# Fibonacci numbers

def brute(n):
    if n <= 1:
        return n
    return brute(n-1) + brute(n-2)

# top down DP

def memoization(n, cache):
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
    return cache[n]

print(memoization(6, {}))

# bottom up DP
# Time: O(N), Space: O(1)
def dp(n):
    if n <= 1:
        return n
    
    start = [0,1]
    
    for i in range(2, n+1):
        temp = start[1]
        start[1] = start[1] + start[0]
        start[0] = temp

    return start[1]

print(dp(5))