'''
6. Crie um dicionário com o nome de três alimentos e suas respectivas calorias.
Peça ao usuário para digitar um alimento e imprima a quantidade de calorias
correspondente.
'''

print("------------------------------ Alimentos -----------------------------")

alimentos = {
    'Maçã': 52,
    'Banana': 96,
    'Cenoura': 41,
}

alimentoDigitado = input("Digite o nome de um alimento: ")

if alimentoDigitado in alimentos:
    calorias = alimentos[alimentoDigitado]
    print(f"{alimentoDigitado} tem {calorias} calorias.")
else:
    print("Alimento não encontrado no dicionário.")

print("----------------------------------------------------------------------")