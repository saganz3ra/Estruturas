'''
4. Crie um dicionário com o nome de três estados e suas respectivas capitais.
Peça ao usuário para digitar um estado e imprima a capital correspondente.
'''

estados_capitais = {
    'Rio Grande do Sul': 'Porto Alegre',
    'Paraná': 'Curitiba',
    'Santa Catarina': 'Florianópolis'
}

print("----------------- Estados e Capitais ---------------")

estado_digitado = input("Digite o nome de um estado: ")

capital = estados_capitais.get(estado_digitado)

if capital:
    print(f"A capital de {estado_digitado} é {capital}.")
else:
    print("Estado não encontrado.")

print("----------------------------------------------------")