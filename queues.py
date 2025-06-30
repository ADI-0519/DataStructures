from collections import deque

q = deque()

print(q)

# To enqueue an element from the right O(1)

q.append(5)
q.append(6)
q.append(8)

print(q)

# Dequeue an object (pop from the left) O(1)

q.popleft()

print(q)

# Peek from left side O(1)

print(q[0])

# Peek from right side O(1)

print(q[-1])