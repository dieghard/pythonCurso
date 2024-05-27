import random
ai = random.randint(1,10)
numero = -1
while numero != ai: 
    numero = int(input("introduce un numero:"))
    if numero< ai:
      print("te pasaste")
    if numero > ai: 
        print("te falto apenas")

print(f"has termiando, el numero era{ai}") 


 