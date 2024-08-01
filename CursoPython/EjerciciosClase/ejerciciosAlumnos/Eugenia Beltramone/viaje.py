print("░█░░░█▀█░░░█▀█░█░█░█▀▀░█▀█░▀█▀░█░█░█▀▄░█▀█░░░█▀▄░█▀▀░░░█▀█░█▀▄░█▀█░█▀▀░█▀▄░█▀█░█▄█░█▀█░█▀▄")
print("░█░░░█▀█░░░█▀█░▀▄▀░█▀▀░█░█░░█░░█░█░█▀▄░█▀█░░░█░█░█▀▀░░░█▀▀░█▀▄░█░█░█░█░█▀▄░█▀█░█░█░█▀█░█▀▄")
print("░▀▀▀░▀░▀░░░▀░▀░░▀░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀░░░▀▀░░▀▀▀░░░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░▀░▀░▀")
print("")
print("")


nombre = input ("Ingresa tu nombre para comenzar esta maravillosa Historia-!!!!!!!: ")
print("")
saludo = print(f"Hola {nombre} vamos a vivir una aventura fascinante!!!!!! Adelante")
print("")
decision_2 = ""
# capitulo 1
capitulo_1 = print("Comienzas el curso de programación y te encuentras con dos profesores entusiastas que te introducen a los conceptos básicos de Python.!!!!! Te enfrentas a desafíos emocionantes y aprendes a escribir tus primeros programas." )
print("")

decision_1 = input ("¿Quieres seguir adelante con el curso?  (Presiona 2 para avanzar al siguiente nivel o 3 para abandonar): ")



while decision_1 != '2' and decision_1 != '3':
    decision_1 = input("Por favor, ingresa una opción válida (2 para continuar, 3 para abandonar): ")
    
# capitulo 2     
if decision_1 == '2': 
    print("")
    print("Capítulo 2: La Aventura Continúa")
    print ("Felicitaciones!!!!! Decides continuar con el curso y te sumerges más profundamente en el mundo de Python.")
    print("Aprendes sobre estructuras de datos, funciones y bucles mientras resuelves problemas cada vez más complejos.")
    print("Tu entusiasmo por la programación crece a medida que adquieres nuevas habilidades.")
    

decision_2 = input("¿Quieres seguir adelante con el curso y enfrentar el desafío del proyecto final? (Presiona 4 para continuar, 3 para abandonar): ")

while decision_2 != '4' and decision_2 != '3':
    decision_2 = input("Por favor, ingresa una opción válida (4 para continuar, 3 para abandonar): ")  
    
if decision_2 == '4':
# Capítulo 3: El Desafío Final
    print(f" {nombre} Llega el momento de enfrentar el proyecto final del curso.")
    print("Te enfrentas a un problema complicado que requiere todas las habilidades que has aprendido hasta ahora.") 
    print("Trabajas duro y, con determinación, logras completar el proyecto con éxito.") 
    print("Tu confianza en tus habilidades de programación está en su punto más alto y estás listo para enfrentar nuevos desafíos en el futuro.") 
    print("¡Felicidades, has alcanzado el Final Feliz!")

else:
    print("Final Triste: Decides abandonar el curso de programación.")
    print("Sin embargo, recuerda que siempre hay oportunidades para aprender y crecer en el mundo de la informática.")