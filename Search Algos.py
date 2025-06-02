
def binary_search(arr,target):
    l,r = 0,len(arr)-1
    
    while l<=r:
        mid = (l+r) // 2
        if target == arr[mid]:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        
        
    return -1

def linear_search(arr,target):
    for i,element in enumerate(arr):
        if element == target:
            return i
    
    return -1

