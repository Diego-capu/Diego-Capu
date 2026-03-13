print("Calcula tu promedio")

reprobados = 0
excelentes = 0
regulares = 0
coder = 0
contador = 0

while  contador < 5 :

    try: 
        modulo = int(input("Ingresa tu modulo: "))
        
        nombre =  input("Ingresa tu nombre: ")

        print(f"Bienvenido: {nombre}")

        ingles = float(input("Ingresa su nota de Ingles: "))
        socio = float(input("Ingresa tu nota de socio: "))
        desarrollo = float(input("Ingresa tu nota de Desarrollo: "))

        if socio <= 100 and ingles <= 100 and  desarrollo <= 100:


            nota1 = ingles * 0.20
            nota2 = socio * 0.20 
            nota3 = desarrollo * 0.60

            resultado = nota1 + nota2 + nota3

            print(f"Modulo {modulo}")
            print(f"Tu promedio es: {resultado}")
            contador = contador + 1

            if 0 <= resultado and resultado < 49:
                reprobados = reprobados + 1
                coder = coder + 1

                print("Reprobado")

            elif 50 <=  resultado and resultado < 79:
                regulares = regulares + 1
                coder = coder + 1

                print("Regular")

            elif resultado >=80:
                excelentes = excelentes + 1
                coder = coder + 1

                print("Excelente")

                
            

           
        else:
            print("No se permiten numeros por encima de 100")

    except ValueError as e:
        print("No se permiten letras")       

print(f"Coders reprobados: {reprobados}")  
print(f"Coders regulares: {regulares}") 
print(f"Coder con promedio excelente: {excelentes}") 
print(f"Numero de coders registrdos: {coder}")    