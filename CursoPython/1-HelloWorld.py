print ("Hola Mundo")
print ("Este es mi super saludo 🖐🏻 con python 🐍")

print("Hola", "mundo", "!")
print(len("Diego")) #= 5



libro = input('Ingrese el nombre del libro:')
autor = input('Ingrese el nombre del autor:')
precio = float(input('Ingrese el precio:'))
envioGratis = input('¿El envio es gratis?/("SI") o ("NO")')

if envioGratis != "SI" and envioGratis != "NO":
   envioGratis="SI"
print (f'''
  Libro : {libro}
  Auto : {autor}
  Precio : {precio}
  envio es gratis: {envioGratis}
''')