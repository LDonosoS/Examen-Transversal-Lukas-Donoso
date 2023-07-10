platinum = 120000
gold = 80000
silver = 50000

asientos = [0] * 100

run = [0] * 100

ganancias = 0

def comprar_entradas():
    global ganancias
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))
    while cantidad < 1 or cantidad > 3:
        print("***DEBE SER ENTRE 1 Y 3***")
        cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))
    print("***UBICACIONES DISPONIBLES***:")
    for i in range(100):
        if asientos[i] == 0:
            print(i+1, end=" ")
        else:
            print("X", end=" ")
        if (i+1) % 10 == 0:
            print()
    for j in range(cantidad):
        print("***VALOR DE ENTRADAS POR POSICION DE ASIENTOS*** \n *(1-20) platinum: $120.000\n *(21-50) gold: $80.000\n *(51-100) silver: $50.000")
        ubicacion = int(input(f"Ingrese la ubicación de asiento deseada {j+1} (entre 1 y 100): "))
        while ubicacion < 1 or ubicacion > 100:
            print("***DEBE SER ENTRE 1 Y 100***")
            print("***VALOR DE ENTRADAS POR POSICION DE ASIENTOS*** \n *(1-20) platinum: $120.000\n *(21-50) gold: $80.000\n *(51-100) silver: $50.000")
            ubicacion = int(input(f"Ingrese la ubicación de asiento deseada {j+1} (entre 1 y 100): "))
        while asientos[ubicacion-1] != 0:
            print("*** LA UBICACION NO ESTA DISPONIBLE***")
            ubicacion = int(input(f"Ingrese la ubicación de asiento deseada {j+1} (entre 1 y 100): "))
        asientos[ubicacion-1] = 1
        run_asist = int(input(f"Ingrese el run del asistente  {j+1} sin '-', '.' y Digito Verif. (ej: 12345678): "))
        while run_asist < 0 or run_asist > 99999999:
            print("***RUN INVALIDO*** \n***DEBE SER UN NUMERO POSITIVO DE MAXIOMO 8 DIGITOS***")
            run_asist = int(input(f"Ingrese el run del asistente {j+1} sin '-', '.' y Digito Verif. (ej: 12345678):"))
        run[ubicacion-1] = run_asist
        if ubicacion <= 20:
            ganancias += platinum
        elif ubicacion <= 50:
            ganancias += gold
        else:
            ganancias += silver
    print("***LA OPERACION SE REALIZO CORRECTAMENTE***")

def mostrar_ubicaciones():
    print("***UBICACIONES DISPONIBLES***")
    for i in range(100):
        if asientos[i] == 0:
            print(i+1, end=" ")
        else:
            print("X", end=" ")
        if (i+1) % 10 == 0:
            print()

def ver_listado():
    run.sort()
    print("Listado de asistentes por RUN:")
    for i in range(100):
        if run[i] != 0:
            print(run[i])

def mostrar_ganancias():
    print(f"Las ganancias totales son ${ganancias}.")

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Comprar de entradas")
    print("2. Ver ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Ver ganancias totales")
    print("5. Salir")

opcion = 0

while opcion != 5:
    mostrar_menu()
    opcion = int(input("Ingrese la opción deseada: "))
    while opcion < 1 or opcion > 5:
        print("***OPCION INVALIDA DEBE SER ENTRE 1 Y 5***")
        opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        comprar_entradas()
    elif opcion == 2:
        mostrar_ubicaciones()
    elif opcion == 3:
        ver_listado()
    elif opcion == 4:
        mostrar_ganancias()
else:
    import datetime 
    fecha = datetime.date.today()
    print(f"***GRACIAS POR USAR EL SISTEMA*** \nMi nombre es Lukas Donoso, su servidor. hoy es {fecha}.")
    
    
#enlace del codigo al GitHub https://github.com/LDonosoS/ET_programacion.git