HP = 100

XP = 0 

NIVEL = 1

historial_tareas = []

print("Bienvenido a tu tracker de hábitos")

#Dibuja una barra de 10 casillas que representa el HP del personaje.
def mostrar_barra_hp(hp_actual):
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
    print("5. Eliminar tarea de historial")
    print("6. Salir")

#Verifica si la opción del menú elegida es valida
def validar_opcion(opcion_texto):
    try:
        numero = int(opcion_texto)
    except ValueError:
        return None
    if numero >= 1 and numero <= 6:
        return numero
    else:
        return None 
#Muestra las tareas del historial numeradas, empezando en 1.
def mostrar_historial():
    for numero, elemento in enumerate(historial_tareas, start=1):
        print(f"{numero}. {elemento}")
   
#Suma la cantidad de XP recibida y revisa si el personaje sube de nivel.
def sumar_xp(cantidad):
    global XP, NIVEL, HP
    XP = XP + cantidad
    if XP >= 100:
        NIVEL = NIVEL + 1
        XP = 0 
        HP = 100
        return True 
    return False

# Muestra el estado inicial y repite el menú hasta que el usuario elija Salir
mostrar_estado()  
opcion = 0 
while opcion != 6:
    mostrar_menu()
    opcion_texto = input("Elige una opción:")
    opcion = validar_opcion(opcion_texto)
    if opcion is None: 
        print("Opción no valida")
        continue 

    if opcion == 1:
        print("Elegiste agregar tarea.")
        nombre_tarea = input ("¿Qué tarea completaste? ")
        while nombre_tarea == "":
            print("Input no válido")
            nombre_tarea = input ("¿Qué tarea completaste? ")
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
        HP = HP - 15 
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
        print("Saliendo del juego")
    




