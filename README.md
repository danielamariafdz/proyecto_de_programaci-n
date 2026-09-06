# Contexto

Es muy importante organizar en algún lugar los deberes que tenemos pendientes y así no olvidarnos. Muchas personas usan listas de tareas o su aplicación de notas para organizarse, pero son bastante aburridos y son fáciles de abandonar porque no dan ninguna sensación de recompensa o progreso. Este proyecto es un rastreador de hábitos pero a modo de juego. El usuario tiene un personaje con puntos de vida (HP) y experiencia (XP). Cada vez que el usuario completa una tarea, su personaje gana experiencia y, al acumular suficiente, sube de nivel. Me parece interesante porque combina los juegos con la organización personal y así hacer rastrear tus hábitos más divertido
Se adjunta el pseudocódigo
https://github.com/danielamariafdz/proyecto_de_programaci-n/blob/main/Avance%201_%20seleccio%CC%81n%20de%20proyecto.pdf

Avance 2:
#Puntos de vida 
hp = 100

#Experiencia 
xp = 0 

#Nivel
nivel = 1 

#Página de Inicio
print("Bienvenido a tu tracker de hábitos")
print(f"Nivel: {nivel}  HP: {hp}  XP: {xp}")

#Mostrar Menú
def mostrar_menu():
    print("1. Agregar tarea completada")
    print("2. Ver estado el personaje")
    print("3. Tarea no completada")
    print("4. Salir")

#Menú 
opcion = 0 
while opcion != 4:
    mostrar_menu()
    opcion = int(input( "Elige una opción:"))

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
    
    elif opcion == 4:
        print("Saliendo del juego")
    else: 
        print("Opción no valida")



