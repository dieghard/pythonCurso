#💻SUMADORA💻 Realizar un programa que permita sumar numeros hasta que se ingrese un 0

print("""  >=>>=>   >=>     >=> >=>       >=>       >>       >====>         >===>      >======>           >>
>=>    >=> >=>     >=> >> >=>   >>=>      >>=>      >=>   >=>    >=>    >=>   >=>    >=>        >>=>
 >=>       >=>     >=> >=> >=> > >=>     >> >=>     >=>    >=> >=>        >=> >=>    >=>       >> >=>
   >=>     >=>     >=> >=>  >=>  >=>    >=>  >=>    >=>    >=> >=>        >=> >> >==>         >=>  >=>
      >=>  >=>     >=> >=>   >>  >=>   >=====>>=>   >=>    >=> >=>        >=> >=>  >=>       >=====>>=>
>=>    >=> >=>     >=> >=>       >=>  >=>      >=>  >=>   >=>    >=>     >=>  >=>    >=>    >=>      >=>
  >=>>=>     >====>    >=>       >=> >=>        >=> >====>         >===>      >=>      >=> >=>        >=>
                                                                                                          """)
print()
sumador=True
sumador_acumulador = 0
while sumador != 0:
    sumador=input("Ingresa cualquier numero, te los sumo hasta que ingreses el cero : ")
    if sumador.isdigit():
        sumador=int(sumador)
    else:
        print ("No sume nada porque no pusiste un numero")
        sumador=True
    sumador_acumulador=sumador+sumador_acumulador
print(f"La suma de todos los numero que ingresaste dió {sumador_acumulador}")