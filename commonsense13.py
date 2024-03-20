import random as rd

#1

def greatestProd(array):
    array.sort()
    return array[-1]*array[-2]*array[-3]

#2

def findMissingNumber(array):
    array.sort()
    for i, x in enumerate(array):
        if i != x:
            return i
        
#3
        
def slowGreat(array):
    
    greatest = 0

    for x in array:
        for y in array:
            if x > y:
                if x > greatest:
                    greatest = x
    return greatest


array = [rd.choice(range(100)) for _ in range(10)]
print(array)

print(slowGreat(array))