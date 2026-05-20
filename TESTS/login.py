# verifica si el rut existe y si esta en el diccionario cliente
def login_clinte():
    rut = input ("Ingrese su rut:")
    if rut not in clientes:
        print ("Error El RUT no fue encontrado")
        return None
    
    cliente = clientes[rut]
    # Aca verifica si el rut de la cuenta creada ya tiene contraseña creada en caso de que no esta creada lo mandara a crear la contraseña
    if cliente["password"] is None :
        print ("Debe de crear una contraseña\n")
        #Obliga al usuario a crear una contraseña y lo tendra que confirmar 
        while True:
            cont1 = input ("Cree contraseña:")
            cont2 = input ("Confirme contraseña:")
            # Avisara que la contraseña ya fue creada exitosamente  
            if cont1 == cont2:
                cliente["password"] = cont1
                print ("La contraseña fue creada exitosamente\n")
                break #la contraseña fue creada exitosamente 
            
            print ("ERROR La contraseña no coencide\nPorfavor reintentar otravez")
        # Ya la contraseña creada tendra que ingresar de nuevo para ser verificada
        while True:
            intentos = input ("Ingrese la contraseña:")
            if intentos == cliente["password"]:
                print (f"Bienveido {cliente["nombre"]}")
                return rut 
            
            print ("La contraseña en incorrecta\n")
