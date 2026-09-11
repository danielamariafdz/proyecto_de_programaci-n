#Puntos de vida 
hp = 100

#Experiencia 
xp = 0 

#Nivel
nivel = 1 

print("Bienvenido a tu tracker de hábitos")

def mostrar_estado():
    print(f"Nivel: {nivel}  HP: {hp}  XP: {xp}")

def mostrar_menu():
    print("1. Agregar tarea completada")
    print("2. Ver estado el personaje")
    print("3. Tarea no completada")
    print("4. Salir")

#Verifica si la opción elegida es valida
def validar_opcion(opcion_texto):
    try:
        numero = int(opcion_texto)
    except:
        return None
    if numero >= 1 and numero <= 4:
        return numero
    else:
        return None 
    
def sumar_xp(cantidad):
    global xp, nivel, hp
    xp = xp + cantidad
    if xp >= 100:
        nivel = nivel + 1
        xp = 0 
        hp = 100
        return True 
    return False

mostrar_estado()  
opcion = 0 
while opcion != 4:
    mostrar_menu()
    opcion_texto = (input("Elige una opción:"))
    opcion = validar_opcion(opcion_texto)
    if opcion is None: 
        print("Opción no valida")
        continue 

    if opcion == 1:
        print("Elegiste agregar tarea.")
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
        print("Saliendo del juego")
    




