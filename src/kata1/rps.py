from random import randint

options = ["Piedra", "Papel", "Tijeras"]


# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    print("Player: "+ player)
    print("AI: "+ ai)
    if player == "piedra" and ai =="tijeras":
        return "Ganaste!"
    elif player == "papel" and ai == "piedra":
        return "Ganaste!"
    elif player == "tijeras" and ai == "papel":
        return "Ganaste!"
    elif player == "tijeras" and ai == "piedra":
        return "Perdiste!"
    elif player == "piedra" and ai == "papel":
        return "Perdiste!"
    elif player == "papel" and ai == "tijeras":
        return "Perdiste!"
    else:
        return "Empate!"
    

# Entry Point
def Game():
    bucle = True
    #
    #
    print("Que empiece el juego...")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")

    while bucle:
        player = input("Elije una opción:").lower()

        if player == "piedra" or player == "papel" or player =="tijeras":
            bucle = False

    ai = options[randint(0, 2)].lower()
    
    
    winner = quienGana(player, ai)

    print(winner)