saldo = 1000
intentos_max = 3
intentos = 0
contraseña_correcta = "1234"

while intentos < intentos_max:
    contraseña = input("Ingrese su contraseña:")
    if contraseña == contraseña_correcta:
        print ("Bienvenido al banco TechBank Riwi Digital")
        print ("Menu de opciones")
        print("1. Consultar saldo")
        print ("2. Retirar")
        print ("3. Depositar")
        print ("4. Salir")
        opcion = input("Seleccione una opcion:")
        if opcion == "1":
            print ("Su saldo es:", saldo)
            
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar:")  )
            if monto <= saldo:
                saldo -= monto
                print ("Retiro exitoso. Su nuevo saldo es:", saldo)
            else:
                print ("Saldo insuficiente")
        elif opcion == "3":
            monto = float(input("Ingrese el monto a depositar:"))
            saldo += monto
            print ("Deposito exitoso. Su nuevo saldo es:", saldo)
        elif opcion == "4":
            print ("Gracias por usar el banco TechBank Riwi Digital")
            break
        else:
            print ("Opcion no valida")
    else:
        intentos += 1
        print ("Contraseña incorrecta. Intentos restantes:", intentos_max - intentos)
        
    
            





