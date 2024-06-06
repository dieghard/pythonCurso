print("")
print("#"*80)
print("######                                                                                       ######")
print("""
      
      
                     __                    __                  __  
| |  >>  |<<   |  | |  | |\ /|  >>  |<<   |  |   |   |  | | | |  | 
|\| |  | --    |  | |><| | < | |  | --    |><|   |   |  | |\| |><| 
| |  <<  >>|    \/  |  | |   |  <<  >>|   |  |   |<< '<<' | | |  | 
 
 
 """)
print("")

seguir = True
contador = 10
num = 1
while seguir:
    contador = int(contador)
    print(f"{contador}")
    contador = contador - num
    if contador == 0:
        print(" DESPEGUE 🚀🚀🚀🚀🚀🚀")
        exit