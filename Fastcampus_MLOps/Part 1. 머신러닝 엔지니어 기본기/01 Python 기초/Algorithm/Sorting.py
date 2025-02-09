def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[i + j] = arr[i]
            j -= 1
        arr[j + 1] = key
        
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)
    less = []
    equal = []
    greater = []
    
    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    
    return quick_sort(less) + equal + quick_sort(greater)


arr = [6, 1, 9, 3, 7, 2, 8, 4, 5]
print(quick_sort(arr))