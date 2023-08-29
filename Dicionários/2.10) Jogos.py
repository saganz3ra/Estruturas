'''
10. Crie um dicionário com o nome de três jogos e a quantidade de jogadores
necessária. Peça ao usuário para digitar um jogo e imprima a quantidade de
jogadores correspondente.
'''

print("------------------------------ Jogos -----------------------------")

jogos = {
    "CS:GO": 10,
    "World of Tanks": 30,
    "DayZ": 10
}

jogo_escolhido = input("Digite o nome de um jogo (CS:GO, World of Tanks ou DayZ): ")

if jogo_escolhido in jogos:
    jogadores_necessarios = jogos[jogo_escolhido]
    print(f"O jogo {jogo_escolhido} requer {jogadores_necessarios} jogadores.")
else:
    print("Jogo não encontrado no dicionário.")

print("------------------------------------------------------------------")