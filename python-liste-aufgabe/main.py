
def cut(lst:list):

    value = None
    for index, x in enumerate(lst):
       
        if (x > 200) & (x % 2 == 0):
            value = x
        
            break
    
    head = lst[:lst.index(value)]
    tail = lst[lst.index(value)-1:]

    return head, value, tail


        
            

lst = [1, 24, -32, 0, -13, 9733, -8, 0, 251, 22, 15423, -974563, 123, 310, -145, -793161, 
1154, 2843, 232, -1]

result = cut(lst)
print (result)

print("head = ",result[0])
print("Value = ",result[1])
print("tail = ",result[2])