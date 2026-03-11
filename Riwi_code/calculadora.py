print ("Calculadora de promedio")
try:
   
        

        ingles = float(input("Ingrese su nota de ingles:"))
        socio = float(input("Ingrese su nota de socio: "))
        desarrollo = float(input("Inhrese su nota de desarrollo: "))

        nota1 = ingles * 0.20
        nota2 = socio * 0.20
        nota3 = desarrollo * 0.60

        resultado = nota1 + nota2 + nota3 

        print(f"Tu promedio es de: {resultado}")

        if resultado >=3.0:
            print ("Aprobaste")
        else:
            print("Reprobaste")

except ValueError as e:
    print("Solo se permiten numeros")