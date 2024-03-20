import time

def badFib(n):
    if n == 0 or n == 1:
        return n
    else:
        return badFib(n-1) + badFib(n-2)

print(badFib(1_1))

def goodFib(n, memo={}):
    if n == 0 or n == 1:
        return n
    
    if n not in memo:
        
        memo[n] = goodFib(n-1, memo) + goodFib(n-2, memo)
    return memo[n]
a = time.perf_counter()
print(goodFib(900))
print(time.perf_counter() - a)

def bottomupFib(n):
    if n == 0:
        return 0
    
    a, b = 0,1

    for i in range(1,n):
        temp = a
        a = b
        b = temp + a
    
    return b
a = time.perf_counter()        
print(bottomupFib(20000))
print(time.perf_counter() - a)