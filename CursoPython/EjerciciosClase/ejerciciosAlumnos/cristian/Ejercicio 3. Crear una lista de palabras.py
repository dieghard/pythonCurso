#Contar cuántas veces aparece una palabra específica en la lista.
#Invertir el orden de la lista.
#Unir dos listas en una sola.
#Dividir una lista en dos sublistas.

nombre_propio =["María", "Pedro", "Juan", "José", "Gabriel", "nicolás", "Isabel", "Héctor",
                 "Lorenzo", "Hugo", "María", "Pedro", "Juan", "José", "Gabriel"]
profesion = ["Camarero/a", "criminalista", "Botánico/a", "Agente de Ventas", 
             "admistrativo", "Astrofísico", "carpintero", "Programador", "Agente de Ventas", 
             "admistrativo", "Astrofísico", "carpintero"]
edades = [15,28,65,45,41,28,13,48,23,33,46]
nombre_propio.reverse ()
profesion.reverse ()
edades.reverse ()
#utilice "title" xk cuando utilice capitalize, me escribia todos los nombres en minuscula
print(f" La lista invertida es: {nombre_propio}".title())
print(f" La lista invertida es: {profesion}".title())
print(f" La lista invertida es: {edades}")

print (f" La lista tiene {edades.count(28)}")

datos_unidos = nombre_propio + profesion 
print (f" Las listas son: {datos_unidos}")

lista_dividida = nombre_propio [0:5] + edades [2:7] + profesion [::-1]
print (f" la lista subdivida es: {lista_dividida}")

    