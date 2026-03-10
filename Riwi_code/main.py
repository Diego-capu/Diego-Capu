saldo = 1000.0
intentos_max = 3
intentos = 0
contraseña_correcta = 1234

while intentos < intentos_max:
    try:
        print ("Bienvenido al banco TechBank Riwi Digital")
        contraseña = int(input("Ingrese su contraseña:"))
        if contraseña == contraseña_correcta:
            print ("Menu de opciones")
            print("1. Consultar saldo")
            print ("2. Retirar")
            print ("3. Depositar")
            print ("4. Salir")
            
            opcion = int(input("Seleccione una opcion:"))
          
            if opcion == 1:
                    print ("Su saldo es:",saldo)
                    print ("Gracias por usar el banco TechBank Riwi Digital")  
                    break                          
            elif opcion == 2:
                monto = float(input("Ingrese el monto a retirar:")  ) 
                if monto <=0:
                    print("No se permiten retiros negativos")
                    print ("Gracias por usar el banco TechBank Riwi Digital")
                    break
                operetiro = saldo - monto
                print(f"Su saldo a retirar fue de: ", monto)
                print("Tu saldo total fue de: ", operetiro)
                break
            elif opcion == 3:
                monto = float(input("Ingrese el monto a depositar:"))
                if monto < 0:
                    print("No se permiten montos negativos")
                    break
                else:
                    saldo += monto
                    print ("Deposito exitoso. Su nuevo saldo es:", saldo)
                    print ("Gracias por usar el banco TechBank Riwi Digital")
                    break
            elif opcion == 4:
                print ("Gracias por usar el banco TechBank Riwi Digital")
                break
            else:
                print ("Opcion no valida")
                break
        else:
            intentos += 1
            print ("Contraseña incorrecta. Intentos restantes:", intentos_max - intentos)
    except ValueError as e:
        print("Ingresa solamente numeros")                
        break          
            
   
            





