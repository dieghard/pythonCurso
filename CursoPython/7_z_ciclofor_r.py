#PRACTICAS
  #1- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS DE 0 A 10

for i in range(11):
  print(i)
  #2- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS DE 10 A 0

for i in range(10, -1, -1):
  print(i)

  #3- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS PARES DE 0 A 10

for i in range(0, 11, 2):
  print(i)

  #4- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS IMPARES DE 0 A 10
  for i in range(1, 11, 2):
    print(i)
  #5- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS PARES DE 0 A 10 Y LUEGO LOS IMPARES DE 0 A 10

  # Mostrar números pares
for i in range(0, 11, 2):
  print(i, "es par")

# Mostrar números impares
for i in range(1, 11, 2):
  print(i, "es impar")

  #6- REALIZAR UN PROGRAMA QUE MUESTRE LA PALABRA ARGENTINA Y POR CADA PALABRA MUESTRE OTRA PALABRA EJEMPLO
  # A rgentina
  # R enacer
  # G loriosa
  # E moción
  # N ación
  # T alento
  # I lusión
  # N ueve
  # A lbiceleste

for palabra in "ARGENTINA":
  #print(palabra)
  if palabra == "A":
      print('A rgentina')
  if palabra == "R":
      print('R enacer')
  if palabra == "G":
      print('G loriosa')
  if palabra == "E":
      print('E moción')
  if palabra == "N":
      print('N ación')
  if palabra == "T":
      print('T alento')
  if palabra == "I":
      print('I lusión')
  if palabra == "N":
      print('N ueve')
  if palabra == "A":
      print('A lbiceleste')
  #else:
  #  print('FIN DEL PROGRAMA')