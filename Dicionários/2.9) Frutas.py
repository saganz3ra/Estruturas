'''
9. Crie um dicionário com o nome de cinco frutas e suas respectivas cores.
Imprima o nome de cada fruta seguido de sua cor.
'''

print("------------------------------ Frutas e Cores -----------------------------")

frutas_cores = {
    "Maçã": "Vermelha",
    "Banana": "Amarela",
    "Laranja": "Laranja",
    "Uva": "Roxa",
    "Limão": "Verde"
}

for fruta, cor in frutas_cores.items():
    print(f"{fruta}: {cor}")

print("---------------------------------------------------------------------------")