'''
4. Crie uma tupla com os nomes de cinco pessoas e peça ao usuário para
digitar um número entre 1 e 5. Imprima o nome correspondente ao número
digitado.
'''

print("--------------- Lista ---------------")

nomes = ("Rafael", "Eduardo", "Allan", "Vittor", "Iuri")
print(nomes)

numero = int(input("Digite um número entre 1 e 5: "))

if numero >= 1 and numero <= 5:
    
    nome_correspondente = nomes[numero - 1]
    print("O nome correspondente é:", nome_correspondente)
else:
    print("Número inválido.")

print("-------------------------------------")