import random as rd
import string

# def intersection(array1, array2):
    
#     dict1={}
#     returnArray = []

#     for i in array1:
#         dict1[i] = True
    
#     for i in array2:
#         if i in dict1:
#             returnArray.append(i)
    
#     return returnArray


# array1, array2 = [rd.choice(range(10)) for _ in range(10)], [rd.choice(range(10)) for _ in range(10)]
# print("array1: ", array1)
# print("array2: ", array2)
# print(intersection(array1, array2))

# def dupe(strArray):

#     dict = {}

#     for s in strArray:
#         if s in dict: 
#             return s
#         else:
#             dict[s] = True


# array = [rd.choice(string.ascii_lowercase) for _ in range(1000)]

# print(array)

# print(dupe(array))

# def missingLetter(weirdString):
    
#     letters={}

#     for c in weirdString:
#         letters[c] = True
    
#     for c in string.ascii_lowercase:
#         if c not in letters:
#             return c



# weirdString="the quick brown box jumps over a lazy dog"
# print(missingLetter(weirdString))

def nondupe(dupeString):
    


    dupes={}

    for c in dupeString:
        dupes[c] = dupes.get(c, 0) + 1

    for c in dupeString:
        if dupes[c] == 1:
            return c

dupeString = "minimum"
print(nondupe(dupeString))        
    
