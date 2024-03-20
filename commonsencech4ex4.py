import random as rd

def greatestNumber(array):

    greatestVal = array[0]

    for i in array:
        if i > greatestVal:
            greatestVal = i
    
    return greatestVal


array = [rd.choice(range(100)) for _ in range(10)]
print(array)
print(greatestNumber(array))


    