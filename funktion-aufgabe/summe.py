
def summe(n:int, m:int):
    
    ######### exemple 1 #############
    res = 0
    for k in range(n, m):
        print("k = ",k)
        res += k
        print("res = ",res)

    return res

result = summe(0,8)

print(result)
