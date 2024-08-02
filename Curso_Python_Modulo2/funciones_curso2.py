import funciones as f 

#numero_1 = f.validar_numero()
#numero_2 = f.validar_numero()
def cliente_nuevo():
    
    
    nombre = f.validar_texto("Ingrese su nombre: ",True,"nombre")
    apellido = f.validar_texto("Ingrese su apellido: ")
    loclaidad = f.validar_texto("Ingrese su localidad: ")
    provincia = f.validar_texto("Ingrese su provincia: ")
    telefono = f.validar_texto ("Ingrese su numero de telefono: ")
    print("Los datos del cliente son : \n")
    if not nombre =="":
        print(f"nombre: {nombre} \n")

    if not apellido =="":
        print(f"apellido: {apellido} \n")
        
    if not loclaidad =="":
        print(f"localidad: {loclaidad} \n")
        
    if not provincia =="":
        print(f"provincia: {provincia} \n")    
        
    if not telefono =="":
        print(f"telefono: {telefono} \n")    
        
    return 

cliente_nuevo()
cliente_nuevo()       

