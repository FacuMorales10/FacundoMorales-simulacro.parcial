
MAX_PACIENTES = 100 # Creamos y definicimos una cantidad finita para el array(se puede modificar si se desea)

pacientes = [None] * MAX_PACIENTES # Primero iniciamos con un "None" para "simular" espacios vacíos.

cantidad_pacientes_actuales = 0 # Creamos la variable para ir llevando el conteo

def mostrar_menu():
    
    print("\nSistema de gestión de Clínica La Fuerza")
    print("1. Cargar pacientes")
    print("2. Mostrar todos los pacientes")
    print("3. Buscar pacientes por número de historial clinico")
    print("4. Ordenar pacientes por número de historial clinico")
    print("5. Mostrar paciente con más dias de internación")
    print("6. Mostrar paciente con menos días de internación")
    print("7. Cantidad de pacientes con más de 5 días de internación")
    print("8. Promedio de días de internación de todos los pacientes")
    print("9. Salir")

def obtener_entero_valido(mensaje):
    """
    simplemente verifica si la entrada es un dígito. Si no lo es, imprime una advertencia y devuelve 0.
    """
    entrada = input(mensaje)
    if entrada.isdigit():
        return int(entrada)
    else:
        print("Entrada inválida. Se espera un numero entero")
        return 0

def cargar_pacientes(lista_pacientes_hosp, num_pacientes_actuales):
    """
    Le permitimos al usuario ingresar los datos de los pacientes
    """
    print("\nCargar Pacientes")
    cantidad_a_ingresar = obtener_entero_valido("Ingrese la cantidad de pacientes a cargar: ")

    if num_pacientes_actuales + cantidad_a_ingresar > MAX_PACIENTES:
        print(f"Error: No se pueden cargar tantos pacientes. Límite actual: {num_pacientes_actuales} / {MAX_PACIENTES}.")
        print(f"Solo quedan {MAX_PACIENTES - num_pacientes_actuales} espacios disponibles.")
        return num_pacientes_actuales 

    for i in range(cantidad_a_ingresar):
        if num_pacientes_actuales < MAX_PACIENTES:
            print(f"\nPaciente N°{num_pacientes_actuales + 1}:")
            historia_clinica = obtener_entero_valido("Número de historial clinico(hasta 4 dígitos): ")
            nombre = input("Nombre del paciente: ")
            edad = obtener_entero_valido("Edad del paciente: ")
            diagnostico = input("Diagnóstico: ")
            dias_internacion = obtener_entero_valido("Cantidad de días de internación: ")

            paciente = [historia_clinica, nombre, edad, diagnostico, dias_internacion]

            lista_pacientes_hosp[num_pacientes_actuales] = paciente
            num_pacientes_actuales += 1 
        else:
            print("Se ha alcanzado el límite máximo de pacientes. No se pueden cargar más.")
            break
    print("Pacientes cargados exitosamente.")
    return num_pacientes_actuales

def mostrar_todos_los_pacientes(lista_pacientes, cantidad_pacientes_actuales):
    """
    Imprime todos los datos de los pacientes almacenados.
    """
    print("\nListado de Pacientes")
    # Si el usuario selecciona cualquier opción sin que existan pacientes registrados, aparecera que no hay pacientes registrados.
    if cantidad_pacientes_actuales == 0:
        print("No hay pacientes registrados para esta operación.")
        return

    print("Historia Clínica | Nombre | Edad | Diagnóstico | Días Internación")
    print("-----------------------------------------------------------------")
    
    for i in range(cantidad_pacientes_actuales):
        paciente = lista_pacientes[i]
        print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]}")

def buscar_paciente_por_historia_clinica(lista_pacientes, cantidad_pacientes_actuales):
    """
    Es una funcion que segun el numero de historial del paciente, le mustra todos sus datos
    """
    print("\nBuscar Paciente por Historia Clínica")
    if cantidad_pacientes_actuales == 0:
        print("No hay pacientes registrados para esta operación.")
        return

    historial_clinico = obtener_entero_valido("Ingrese el número de historial clínico del paciente (4 dígitos): ")
    encontrado = False
    # Iteramos solo sobre la cantidad de pacientes que realmente hemos cargado
    for i in range(cantidad_pacientes_actuales):
        paciente = lista_pacientes[i]
        if paciente[0] == historial_clinico:
            print("\nPaciente Encontrado:")
            print(f"Número de Historia Clínica: {paciente[0]}")
            print(f"Nombre: {paciente[1]}")
            print(f"Edad: {paciente[2]}")
            print(f"Diagnóstico: {paciente[3]}")
            print(f"Días de Internación: {paciente[4]}")
            encontrado = True
            return
    if not encontrado:
        print(f"No se encontró ningún paciente con la Historia Clínica {historial_clinico}.")

def ordenar_pacientes_por_historia_clinica(lista_pacientes, cantidad_pacientes_actuales):
    """
    Es una función que ordena la lista de pacientes segun su numero de pacientee en forma ascendente.
    """
    print("\nOrdenar Pacientes por Historial Clínico")
    if cantidad_pacientes_actuales == 0:
        print("No hay pacientes registrados para esta operación.")
        return

    n = cantidad_pacientes_actuales
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Esto compara el número de historia clínica 
            if lista_pacientes[j][0] > lista_pacientes[j + 1][0]:
                # Intercambio de elementos
                elem = lista_pacientes[j]
                lista_pacientes[j] = lista_pacientes[j + 1]
                lista_pacientes[j + 1] = elem
    print("Pacientes ordenados por número de historial clinico(ascendente).")
    mostrar_todos_los_pacientes(lista_pacientes, cantidad_pacientes_actuales) # Muestra la lista ordenada

def mostrar_paciente_con_mas_dias_internacion(lista_pacientes, cantidad_pacientes_actuales):
    """
    Calcula e imprime el paciente con más días de internación, tambien mustra todos sus datos.
    """
    print("\nPaciente con más días de internación")
    if cantidad_pacientes_actuales == 0:
        print("No hay pacientes registrados para esta operación.")
        return

    # Inicializamos con el primer paciente cargado
    paciente_mas_dias = None
    max_dias = -1

    for i in range(cantidad_pacientes_actuales):
        if lista_pacientes[i] != None:
            paciente_mas_dias = lista_pacientes[i]
            max_dias = int(paciente_mas_dias[4])
            break

    if paciente_mas_dias == None:
        print("No se encontraron pacientes validos")
        return
    
    for i in range(cantidad_pacientes_actuales):
        paciente_1 = lista_pacientes[1]
        if paciente_1 != None and int(paciente_1[4]) > max_dias:
            max_dias = int(paciente_1[4])
            paciente_mas_dias = paciente_1

    print("\nPaciente con la mayor cantidad de días de internación")
    print(f"Número de Historia Clínica: {paciente_mas_dias[0]}")
    print(f"Nombre: {paciente_mas_dias[1]}")
    print(f"Edad: {paciente_mas_dias[2]}")
    print(f"Diagnóstico: {paciente_mas_dias[3]}")
    print(f"Días de Internación: {paciente_mas_dias[4]}")

def mostrar_paciente_con_menos_dias_internacion(lista_pacientes, cantidad_pacientes_actuales):
    """
    Calcula e imprime el paciente con menos dias de internación, tambien muestra todos sus datos.
    """
    print("\nPaciente con menos días de internación")
    if cantidad_pacientes_actuales == 0:
        print("No hay pacientes registrados para esta operación.")
        return

    # Inicializamos con el primer paciente cargado
    paciente_menos_dias = None
    min_dias = -1 

    for i in range(1, cantidad_pacientes_actuales):
        if lista_pacientes[i] != None:
            paciente_menos_dias = lista_pacientes[i]
            min_dias = int(paciente_menos_dias[4])
        break
    
    if paciente_menos_dias == None:
        print("No se encontró ningun paciente válido")
        return
    
    for i in range(cantidad_pacientes_actuales):
        paciente_actual = lista_pacientes[i]
        if paciente_actual != None and int (paciente_actual[4]) < min_dias:
            min_dias = int(paciente_actual[4])
            paciente_menos_dias = paciente_actual

    print("\nPaciente con la menor cantidad de días de internación")
    print(f"Número de Historia Clínica: {paciente_menos_dias[0]}")
    print(f"Nombre: {paciente_menos_dias[1]}")
    print(f"Edad: {paciente_menos_dias[2]}")
    print(f"Diagnóstico: {paciente_menos_dias[3]}")
    print(f"Días de Internación: {paciente_menos_dias[4]}")

def contar_pacientes_mas_de_5_dias(lista_pacientes, cantidad_pacientes_actuales):
    """
    Es un funcion que muestra a los pacientes que tienen mas de 5 días de intenación
    """
    print("\nCantidad de Pacientes con más de 5 Días de Internación")
    if cantidad_pacientes_actuales == 0:
        print("No hay pacientes registrados para esta operación.")
        return

    contador = 0

    for i in range(cantidad_pacientes_actuales):
        paciente = lista_pacientes[i]
        if paciente[4] > 5: # Días de internación es el índice 4
            contador += 1
    print(f"Cantidad de pacientes con más de 5 días de internación: {contador}")

def calcular_promedio_dias_internacion(lista_pacientes,cantidad_pacientes_actuales):
    """
    Calcula el promedio de días de internación de todos los pacientes registrados.
    """
    print("\nPromedio de Días de Internación")
    if cantidad_pacientes_actuales == 0:
        print("No hay pacientes registrados para esta operación.")
        return

    total_dias = 0

    for i in range(cantidad_pacientes_actuales):
        paciente = lista_pacientes[i]
        total_dias += paciente[4] # Días de internación es el índice 4

    promedio = total_dias / cantidad_pacientes_actuales
    print(f"El promedio de días de internación de todos los pacientes es: {promedio} días")


# (INICIO DEL PROGRAMA PRINCIPAL)

ejecutando = True
cantidad_pacientes_actuales = 0 

while ejecutando:
    mostrar_menu()
    opcion = obtener_entero_valido("Seleccione una opción: ")

    if opcion == 1:
        cantidad_pacientes_actuales = cargar_pacientes(pacientes, cantidad_pacientes_actuales)
    elif opcion == 2:
        mostrar_todos_los_pacientes(pacientes, cantidad_pacientes_actuales)
    elif opcion == 3:
        buscar_paciente_por_historia_clinica(pacientes, cantidad_pacientes_actuales)
    elif opcion == 4:
        ordenar_pacientes_por_historia_clinica(pacientes, cantidad_pacientes_actuales)
    elif opcion == 5:
        mostrar_paciente_con_mas_dias_internacion(pacientes, cantidad_pacientes_actuales)
    elif opcion == 6:
        mostrar_paciente_con_menos_dias_internacion(pacientes, cantidad_pacientes_actuales)
    elif opcion == 7:
        contar_pacientes_mas_de_5_dias(pacientes, cantidad_pacientes_actuales)
    elif opcion == 8:
        calcular_promedio_dias_internacion(pacientes, cantidad_pacientes_actuales)
    elif opcion == 9:
        print("Saliendo del sistema. ¡Hasta pronto!")
        ejecutando = False
    else:
        print("Opción no válida. Por favor, intente de nuevo.")