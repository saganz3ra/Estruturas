'''
5. Crie um dicionário com o nome de cinco cidades e suas respectivas
populações. Imprima a cidade com a maior população.
'''

print("------------------------------ População -----------------------------")

cidades = {
    'Guarapuava': 180000,
    'Porto Alegre': 1500000,
    'Florianópolis': 500000,
}

maior_populacao = max(cidades, key=cidades.get)

print(f"A cidade com a maior população é {maior_populacao} com {cidades[maior_populacao]} habitantes.")

print("----------------------------------------------------------------------")