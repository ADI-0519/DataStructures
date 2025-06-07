
def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                sorted = False

    return arr
                
def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = item

    return arr




           