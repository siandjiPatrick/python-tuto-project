
def summe(n:int, m:int):
    
    ######### methode 2 #############

    list_result = []
    for k in range(n, (m+1)+1):

        res = 2**(2*k)
        print("pour k = ", k , "--> 2^2*",k, "= ",res)

        # Fügen wir das Ergebnis in die Liste ein
        list_result.append(res)
        
    return list_result

############### hauptprogramm ##################

print("\n!!! n und m müssen ganze zahl sein ")

# Benutzer Interaktion
n = int(input("geben Sie n ein -->  "))  # 
m = int(input("geben Sie m ein -->  "))

result = summe(n,m)

summe_result = sum(result)
print("Die Summe ergibt : ", summe_result)

