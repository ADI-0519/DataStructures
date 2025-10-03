stk = []

# Pushing to stack

stk.append(4)
stk.append(5)


# Ask if stack empty

if stk:
    print(True)


# Pop from stack O(1)

if stk:
    print(stk.pop())


# Peek from stack

print(stk[-1])


# Create a montonically decreasing stack
arr = [2,1,3,2,4,3]
n = len(arr)
stk = []
res = [-1] * n

for i in range(n):
    while stk and arr[i] > arr[stk[-1]]: 
        index = stk.pop()
        res[index] = arr[i]

    stk.append(i)

print(res)

# Create a monotonically increasing stack.

result = [-1] * n
stk = []

for i in range(n):
    while stk and arr[i] < arr[stk[-1]]:
        index = stk.pop()
        result[index] = arr[i]

    stk.append(i)

print(result)

res = [-1] * n
stk = []