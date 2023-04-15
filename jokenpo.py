import random

def tesoura():    
    print("   _    _")
    print("  (_)  / )")
    print("    | (_/")
    print("   _+/")
    print("  //|\\")
    print(" // ||")
    print("(/  |/")

def pedra():
    print("   ____")
    print(" _/  _ \\")
    print("/ _ - _ \\")
    print("\\_______/")

def papel():
    print("    _____")
    print("   O_____O")
    print("  /     /")
    print(" /____ /")
    print("O_____O")

def mostraJogada(player, maquina):
    print("\n\nVocê: ")
    if player == 0:
        pedra()
    elif player == 1:
        papel()
    else:
        tesoura()
    print("\nMáquina: ")
    if maquina == 0:
        pedra()
    elif maquina == 1:
        papel()
    else:
        tesoura()

def mostraPlacar(placar):
    print(f"Vitórias: {placar[0]}\nDerrotas: {placar[1]}\nEmpates: {placar[2]}")

def jokenpo(player, maquina, placar):
    pass

           

#A lista placar é: Vitórias, Derrotas, Empates
placar = [0,0,0]
gameOn = "sim"
while gameOn.lower() == "sim":
    pass