import random

def jugar_piedra_papel_tijera():
    opciones = ["Piedra", "Papel", "Tijeras"]
    eleccion_computadora = random.choice(opciones)
    eleccion_usuario = input("Elige Piedra, Papel o Tijeras: ").capitalize() # Capitalize para manejar mayúsculas/minúsculas

    print(f"Tú elegiste: {eleccion_usuario}")
    print(f"La computadora eligió: {eleccion_computadora}")

    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif eleccion_usuario == "Piedra":
        if eleccion_computadora == "Tijeras":
            print("¡Piedra aplasta a Tijeras! ¡Ganaste!")
        else:
            print("¡Papel cubre a Piedra! ¡Perdiste!")
    elif eleccion_usuario == "Papel":
        if eleccion_computadora == "Piedra":
            print("¡Papel cubre a Piedra! ¡Ganaste!")
        else:
            print("¡Tijeras cortan a Papel! ¡Perdiste!")
    elif eleccion_usuario == "Tijeras":
        if eleccion_computadora == "Papel":
            print("¡Tijeras cortan a Papel! ¡Ganaste!")
        else:
            print("¡Piedra aplasta a Tijeras! ¡Perdiste!")
    else:
        print("Opción no válida. Intenta de nuevo.")

# Para ejecutar el juego:
jugar_piedra_papel_tijera()