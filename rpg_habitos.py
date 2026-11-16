HP = 100

XP = 0 

NIVEL = 1

historial_tareas = [] 

habitos = ["Ejercicio", "Leer", "Agua"]

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

semana = [[0] * len(dias) for _ in range(len(habitos))]

print("Bienvenido a tu tracker de hábitos")

#Dibuja una barra de 10 casillas que representa el HP del personaje.
def mostrar_barra_hp(hp_actual):
    hp_actual = max(0, min(100, hp_actual))
    llenas = hp_actual // 10
    for i in range(llenas):
        print("■", end="")
    vacias = 10 - llenas
    for i in range(vacias):
        print("□", end="")
    print()
    
#Muestra el estado actual del jugador
def mostrar_estado():
    print(f"Nivel: {NIVEL} XP: {XP}")
    print("HP:", end=" ")
    mostrar_barra_hp(HP)

#Muestra el menú del juego
def mostrar_menu():
    print("1. Agregar tarea completada")
    print("2. Ver estado del personaje")
    print("3. Tarea no completada")
    print("4. Ver historial de tareas")
    print("5. Eliminar tarea del historial")
    print("6. Ver semana de hábitos")
    print("7. Marcar hábito de la semana")
    print("8. Salir")
    print("9. Buscar tareas en el historial")

#Verifica si la opción del menú elegida es valida
def validar_opcion(opcion_texto):
    try:
        numero = int(opcion_texto)
    except ValueError:
        return None
    if numero >= 1 and numero <= 9:
        return numero
    else:
        return None 

def pedir_numero(mensaje, maximo):
    texto = input(mensaje)
    try:
        numero = int(texto)
    except ValueError:
        return None
    if numero >= 1 and numero <= maximo:
        return numero
    return None

#Muestra las tareas del historial numeradas, empezando en 1.
def mostrar_historial():
    for numero, elemento in enumerate(historial_tareas, start=1):
        print(f"{numero}. {elemento}")

def mostrar_semana(matriz):
    print(" " * 10, end="")
    for dia in dias:
        print(f"{dia:<4}", end="")
    print()
    for i in range(len(matriz)):
        print(f"{habitos[i]:<10}", end="")
        for valor in matriz[i]:
            print(f"{valor:<4}", end="")
        print()
   
#Suma la cantidad de XP recibida y revisa si el personaje sube de nivel.
def sumar_xp(cantidad):
    global XP, NIVEL, HP
    XP = XP + cantidad
    subio_nivel = False
    while XP >= 100:
        NIVEL = NIVEL + 1
        XP = XP - 100
        HP = 100
        subio_nivel = True
    return subio_nivel

# Avance 8: manejo de cadenas.
# strip elimina espacios de los extremos; split separa las palabras y
# join las vuelve a unir con un solo espacio, conservando su escritura.
def limpiar_texto(texto):
    return " ".join(texto.strip().split())


# lower permite comparar textos sin distinguir mayúsculas de minúsculas.
# El operador in encuentra una palabra o fragmento dentro de cada tarea.
def buscar_tareas(consulta):
    consulta = limpiar_texto(consulta).lower()
    if consulta == "":
        print("Escribe una palabra o un fragmento para buscar.")
        return

    coincidencias = 0
    for numero, tarea in enumerate(historial_tareas, start=1):
        if consulta in tarea.lower():
            print(f"{numero}. {tarea}")
            coincidencias = coincidencias + 1

    if coincidencias == 0:
        print(f'No se encontraron tareas que contengan "{consulta}".')
    else:
        print(f"Coincidencias encontradas: {coincidencias}")


# Muestra el estado inicial y repite el menú hasta que el usuario elija Salir
mostrar_estado()  
opcion = 0 
while opcion != 8:
    mostrar_menu()
    opcion_texto = input("Elige una opción:")
    opcion = validar_opcion(opcion_texto)
    if opcion is None: 
        print("Opción no valida")
        continue 

    if opcion == 1:
        print("Elegiste agregar tarea.")
        nombre_tarea = limpiar_texto(input("¿Qué tarea completaste? "))
        while nombre_tarea == "":
            print("Escribe una tarea; no puede contener solo espacios.")
            nombre_tarea = limpiar_texto(input("¿Qué tarea completaste? "))
        historial_tareas.append(nombre_tarea)
        subio_nivel = sumar_xp(10)
        if subio_nivel:
            print("¡Subiste de nivel! Tu HP se restauró!")
        else:
            print(f"Ganaste 10 XP. XP actual: {XP}")

    elif opcion == 2:
        print("Elegiste ver el estado del personaje")
        mostrar_estado()

    elif opcion == 3:
        HP = max(0, HP - 15)
        print(f"Perdiste 15 HP. HP actual: {HP}")
        if HP <= 0:
            print("GAME OVER!")
            HP = 100
            XP = 0 
            NIVEL = 1
            break 

    elif opcion == 4:
        if not historial_tareas:
            print("Aún no has completado ninguna tarea.")
        else:
            if len(historial_tareas) == 1:
                print(f"Has completado {len(historial_tareas)} tarea")
            else:
                print(f"Has completado {len(historial_tareas)} tareas")
            print("Tus tareas completadas: ")
        mostrar_historial()

    elif opcion == 5:
        if not historial_tareas:
            print("Aún no has completado ninguna tarea.")
        else:
            mostrar_historial()
            numero_texto = input("¿Qué tarea quieres eliminar? (escribe el número): ")
            try:
                posicion = int(numero_texto)
            except ValueError:
                print("Debes escribir un número.")
            else:
                if posicion >= 1 and posicion <= len(historial_tareas):
                    eliminada = historial_tareas.pop(posicion - 1)
                    print(f"Eliminaste: {eliminada}")
                else:
                    print("Ese número no está en la lista.")
    
    elif opcion == 6:
        mostrar_semana(semana)
    
    elif opcion == 7:
        mostrar_semana(semana)
        for numero, habito in enumerate(habitos, start=1):
            print(f"{numero}. {habito}")
        fila = pedir_numero("Número del hábito: ", len(habitos))
        for numero, dia in enumerate(dias, start=1):
            print(f"{numero}. {dia}")
        columna = pedir_numero("Número del día: ", len(dias))
        if fila is None or columna is None:
            print("Número no válido.")
        elif semana[fila - 1][columna - 1] == 1:
            print("Ya marcaste ese hábito ese día.")
        else:
            semana[fila - 1][columna - 1] = 1
            print(f"Marcaste {habitos[fila - 1]} el {dias[columna - 1]}.")
            subio_nivel = sumar_xp(10)
            if subio_nivel:
                print("¡Subiste de nivel! Tu HP se restauró!")
            else:
                print(f"Ganaste 10 XP. XP actual: {XP}")

    elif opcion == 8:
        print("Saliendo del juego")

    elif opcion == 9:
        if not historial_tareas:
            print("Aún no has completado ninguna tarea.")
        else:
            consulta = input("¿Qué palabra o fragmento quieres buscar? ")
            buscar_tareas(consulta)
