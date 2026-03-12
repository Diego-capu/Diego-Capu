

bedida = input("Que bedida desea: ")
cantidad = int(input("Que cantidad desea: "))


if bedida == "cafe":
    precio = 4000
elif bedida == "te":
    precio = 3500
elif bedida == "jugo":
    precio = 5000


    resultado = precio * cantidad

    print(f"Total a pagar {resultado}")
    


