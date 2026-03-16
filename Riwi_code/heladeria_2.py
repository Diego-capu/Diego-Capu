print("Heladeria")
print("Productos")
print("Cono, Vaso, Banana")
customers = 0
total = 0
cone = 0
glass = 0
banana = 0

while True:
    try:
        product =  input("Ingrese su producto--Si no desea realizar mas pedidos escriba (1): ")
        if product == "1":
            break
        if product == "cono" :
            print("cono = 3000")
            quantity = int(input("Ingrese su cantidad: "))
            total1 = 3000 * quantity
            total = total + total1
            cone = cone + quantity
            customers = customers + 1
            print(f"Total a pagar:{total1}")
        elif product == "vaso" :
            print("Vaso = 4000")
            quantity = int(input("Ingrese su cantidad: "))
            total1 = 4000 * quantity
            total = total + total1
            glass = glass + quantity
            customers = customers + 1
            print(f"Total a pagar:{total1}")
        elif product == "banana" :
            print("Banana = 9000")
            quantity = int(input("Ingrese su cantidad: "))
            total1 = 9000 * quantity
            total = total + total1
            banana = banana + quantity
            customers = customers + 1
            print(f"Total a pagar:{total1}")
        else:

            print("Valor invalido")
            break
    except ValueError as e:
        print("Valor invalido")


if cone > glass and cone > banana :
    print(f"Cantidad de clieten atendidos: {customers}")
    print(f"Total vendio {total}")
    print(f"Que producto se pidio mas veces fue cono:  {cone}")
elif glass > cone and glass > banana:
    print(f"Cantidad de clieten atendidos: {customers}")
    print(f"Total vendio {total}")
    print(f"Que producto se pidio mas veces fue vaso:  {glass}")
elif banana > cone and banana > glass:
    print(f"Cantidad de clieten atendidos: {customers}")
    print(f"Total vendio {total}")
    print(f"Que producto se pidio mas veces fue banana:  {banana}")


        
