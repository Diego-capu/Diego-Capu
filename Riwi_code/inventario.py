#Evita que se puedan ingresar datos invalidos 
try:
    #solicitar datos al usuario
    nombre = input("Ingrese su nombre: ")
    precio = float(input("Ingrese su preicio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    #Realiza la operacion y almacena el resultado
    costo_total = precio * cantidad

    #Imprime los resultados
    print(f"Nombre del producto: {nombre}")
    print(f"Precio del producto: {precio}")
    print(f"Cantidad del producto: {cantidad}")
    print(f"Costo total: {costo_total}")



except ValueError as  e:
    print("Valor invalido")

