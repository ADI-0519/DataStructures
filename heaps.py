# Build a min heap from a list of elements.
# time complexity: O(n), space complexity: O(1)
import heapq
from collections import Counter

A = [-4,3,1,0,2,5,10,8,12,9]
heapq.heapify(A)

# Print the heapified list
print(A)

# Heappush the element

heapq.heappush(A, 4)
print(A)

# Heappop the smallest element
print(heapq.heappop(A))
print(A)

# Heap peek

print(A[0])  # The smallest element in the heap

# Heap sort
def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        min_item = heapq.heappop(arr)
        new_list[i] = min_item

    return new_list

# Making a max heap

B = [-4,3,1,0,2,5,10,8,12,9]

n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)

largest = -heapq.heappop(B)


# heap pushing 7 into the max heap
heapq.heappush(B, -7)
print(B)

# Building a heap from scratch

C = [-5,4,2,1,7,0,3]

def build_heap(arr):
    heap = []
    n = len(arr)

    for i in range(n):
        heapq.heappush(heap, arr[i])
        print(heap)

    return heap

build_heap(C)

# Placing tuples in a heap

D = [5,4,3,5,4,3,5,5,4]
counter = Counter(D)
print(counter)
heap = []
for i,j in counter.items():
    heapq.heappush(heap, (j, i))

print(heap)