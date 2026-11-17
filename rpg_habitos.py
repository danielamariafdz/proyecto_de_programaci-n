hp = 100

xp = 0 

nivel = 1

nombre_jugador = ""

historial_tareas = [] 

habitos = ["Ejercicio", "Leer", "Agua"]

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

semana = [[0] * len(dias) for _ in range(len(habitos))]

#Dibuja una barra de 10 casillas que representa el HP del personaje.
def mostrar_barra_hp(hp_actual):
    llenas = hp_actual // 10
    for i in range(llenas):
        print("■", end="")
    vacias = 10 - llenas
    for i in range(vacias):
        print("□", end="")
    print()
    
def mostrar_estado():
    print(f"Jugador: {nombre_jugador.upper()}")
    print(f"Nivel: {nivel} XP: {xp}")
    print("HP:", end=" ")
    mostrar_barra_hp(hp)

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

#Verifica si la opción del menú elegida es valida
def validar_opcion(opcion_texto):
    try:
        numero = int(opcion_texto)
    except ValueError:
        return None
    if numero >= 1 and numero <= 8:
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
    global xp, nivel, hp
    xp = xp + cantidad
    if xp >= 100:
        nivel = nivel + 1
        xp = 0 
        hp = 100
        return True 
    return False

#Muestra el estado actual del jugador
def main():
    global hp, nombre_jugador
    nombre_jugador = input("¿Cómo te llamas? ")
    print(f"¡Bienvenido a tu tracker de hábitos {nombre_jugador.capitalize()}!")
    
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
            nombre_tarea = input ("¿Qué tarea completaste? ")
            while nombre_tarea == "":
                print("Input no válido")
                nombre_tarea = input ("¿Qué tarea completaste? ")
            historial_tareas.append(nombre_tarea)
            subio_nivel = sumar_xp(10)
            if subio_nivel:
                print("¡Subiste de nivel! Tu HP se restauró!")
            else:
                print(f"Ganaste 10 XP. XP actual: {xp}")

        elif opcion == 2:
            print("Elegiste ver el estado del personaje")
            mostrar_estado()

        elif opcion == 3:
            hp = hp - 15 
            print(f"Perdiste 15 HP. HP actual: {hp}")
            if hp <= 0:
                print("GAME OVER!")
                hp = 100
                xp = 0 
                nivel = 1
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
                    print(f"Ganaste 10 XP. XP actual: {xp}")

        elif opcion == 8:
            print("Saliendo del juego")
    
if __name__ == "__main__":
    main()



