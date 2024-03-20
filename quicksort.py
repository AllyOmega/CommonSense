import random as rd

#Lomuto partition scheme, more straightforward
#more swaps, less efficient?
def partition(array,p,r):

    x = array[r]
    
    i = p - 1
    
    for j in range(p, r):
        if array[j] <= x:
            i += 1
   
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[r]= array[r], array[i+1]
    return i + 1

#Hoare partition scheme, more efficient
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



def quicksort(array, p, r):
    
    if p < r:
        q = compart(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)
    

array = [0,5,2,1,6,3]#[rd.choice(range(100)) for _ in range(10)]
print(array)
quicksort(array, 0, len(array) - 1)
print(array)
