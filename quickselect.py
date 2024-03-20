
import random as rd 

def compart(array, l, r):
    pivot_index = r

    pivot = array[r]

    r -= 1

    while True:
        while array[l] < pivot:
            l += 1
        while array[r] > pivot:
            r -= 1
    
        if l >= r:
            break
        else:
            array[l], array[r] = array[r], array[l]

            l += 1
    
    array[l], array[pivot_index] = array[pivot_index], array[l]

    return l

def quickselect(array, k, l, r):

    if r - l<= 0:
        return array[l]
    
    p = compart(array, l, r)
    if k == p:
        return array[p]
    elif k < p:
        return quickselect(array, k, l, p - 1)
    elif k > p:
        return quickselect(array, k, p + 1, r)

    


array = [rd.choice(range(100)) for _ in range(10)]
print(array)
arraycp = array.copy()
arraycp.sort()
print(arraycp)

print(quickselect(array, 5, 0, len(array) - 1))

