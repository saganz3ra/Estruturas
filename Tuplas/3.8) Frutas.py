'''
8. Crie uma tupla com os nomes de cinco frutas e suas respectivas cores.
Imprima o nome de cada fruta seguido de sua cor.
'''

print("------- Frutas -------")

frutas_cores = (
    ("Maçã", "vermelho"),
    ("Banana", "amarelo"),
    ("Laranja", "laranja"),
    ("Uva", "roxo"),
    ("Morango", "vermelho")
)

for fruta, cor in frutas_cores:
    print(fruta, "-", cor)

print("----------------------")