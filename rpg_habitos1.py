#Puntos de vida 
hp = 100

#Experiencia 
xp = 0 

#Nivel
nivel = 1 

print("Bienvenido a tu tracker de hábitos")
print(f"Nivel: {nivel}  HP: {hp}  XP: {xp}")

def mostrar_menu():
    print("1. Agregar tarea completada")
    print("2. Ver estado el personaje")
    print("3. Tarea no completada")
    print("4. Salir")
  
opcion = 0 
while opcion != 4:
    mostrar_menu()
    opcion = int(input("Elige una opción:"))

    if opcion == 1:
        print("Elegiste agregar tarea.")
        xp = xp + 10 
        print(f"Ganaste 10 XP. XP actual: {xp}")
        if xp >= 100:
            nivel = nivel + 1
            xp = 0 
            hp = 100
            print(f"Subiste de nivel! Tu HP se restauró!")
    elif opcion == 2:
        print("Elegiste ver el estado del personaje")
        print(f"Nivel: {nivel}  HP: {hp}  XP: {xp}")
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
    else: 
        print("Opción no valida")