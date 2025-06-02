
def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                sorted = False
                
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)-1):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]




           