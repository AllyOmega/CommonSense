import random as rd

def bubble_sort(array):

    unsorted_until_index = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
                
        unsorted_until_index -= 1

    return array

# def insertion_sort(array):
#     for i in range(1, len(array)):
#         temp = array[i]
#         array[i] = None

#         for j in range(i - 1,-1,-1):
#             if array[j] > temp:
#                 array[j+1] = array[j]
#                 array[j] = None
#             elif array[j] <= temp:
#                 array[j + 1] = temp
#                 break

#             if j == 0:
#                 array[j] = temp

#     return array

def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]

        j = i - 1
        
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
        



    print(array)
#array = [rd.choice(range(100)) for _ in range(10)]
array = [75, 70, 99, 81, 3, 85, 9, 38, 86, 75]
print(array)
#print(bubble_sort(array))
print(insertion_sort(array))

