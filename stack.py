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


