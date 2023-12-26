
def summe(n:int, m:int):
    
    ######### Summe #############

    list_result = []
    for k in range(n, (m+1)+1):

        res = 2**(2*k)
        print("fuer k = ", k , "--> 2^2*",k, "= ",res)

        # Fügen wir das Ergebnis in die Liste ein
        list_result.append(res)
        
    return list_result

############### hauptprogramm ##################




error_input = True
while error_input:
    try :
        print("\nGeben Sie n und m ein(n und m müssen ganze Zahl sein): ")
        # Benutzer Interaktion
        n = int(input("geben Sie n ein -->  "))  # 
        m = int(input("geben Sie m ein -->  "))
        print(type(n))
        print(type(n))

    except KeyboardInterrupt:
        print("\nprogramm wurde beendet")
        exit()
    except:
        print("\n!!! Eingabe falsch ")
    else:
        error_input = False
        print("else")


result = summe(n,m)

summe_result = sum(result)
print("Die Summe ergibt : ", summe_result)

