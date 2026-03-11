print("Calcula tu promedio")

contador = 0
while contador == 0:

    try: 
        modulo = int(input("Ingresa tu modulo: "))
        nombre = str(input("Ingresa tu nombre: "))
        print(f"Bienvenido: {nombre}")

        ingles = float(input("Ingresa su nota de Ingles: "))
        socio = float(input("Ingresa tu nota de socio: "))
        desarrollo = float(input("Ingresa tu nota de Desarrollo: "))

        if socio and ingles <= 100:


            nota1 = ingles * 0.20
            nota2 = socio * 0.20 

            if desarrollo <=100:

                nota3 = desarrollo * 0.60
            else:
                print("No se permiten numeros por encima de 100")
            


                resultado = nota1 + nota2 + nota3 
                if resultado >= 80:
                    print("Excelente")

                elif resultado >=50:
                    print("Regular") 
                elif resultado <= 49:
                    print("Reprobado")

                print(f"Tu promedio es de {resultado}")
        else:
            print("No se permiten numeros por encima de 100")

