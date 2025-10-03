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


# Use a monotonic stack for problems that involve finding the next/previous greater/smaller element for each item in a sequence or for 
# problems like the Next Greater Element problem and Largest Rectangle in a Histogram. Use a monotonic queue for optimizing 
# sliding window problems where you need to efficiently find the minimum or maximum within a moving window, such as in sliding window maximum/minimum problems
# We use queue as we need to add/remove elements from beginning and end in O(1)

# general code for decreasing queue:


output = []
arr = [1,3,-1,-3,5,3,6,7]
q2 = deque()
k = 3

for i in range(k):
    
    while q2 and arr[q2[-1]] <= arr[i]:
        q2.pop()

    q2.append(i)

output.append(arr[q2[0]])

# now let's add element on at a time

for i in range(k,len(arr)):

    while q2 and q2[0] <= i-k:
        q2.popleft()

    while q2 and arr[q2[-1]] <= arr[i]:
        q2.pop()

    q2.append(i)
    output.append(arr[q2[0]])

print(output)