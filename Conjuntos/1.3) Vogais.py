'''
3. Crie um conjunto com as vogais (a, e, i, o, u) e peça ao usuário para digitar
uma palavra. Imprima as vogais que aparecem na palavra digitada.
'''

vogais = {'a', 'e', 'i', 'o', 'u'}

print("--------------- Vogais ---------------")
palavra = input("Digite uma palavra: ")

vogais_presentes = set(filter(lambda letra: letra in vogais, palavra))
print("Vogais presentes na palavra:", ', '.join(vogais_presentes))

print("--------------------------------------")