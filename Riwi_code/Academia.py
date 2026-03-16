print("Ingrese su asistencia")
while True:
    attendance = int(input("-"))

    if attendance < 5:
        print("Asistencia baja")
    elif 5 <= attendance and attendance < 8:
        print("Asistencia media")
    elif attendance >= 9:
        print("Asistencia alta")