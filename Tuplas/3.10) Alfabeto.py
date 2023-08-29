'''
10. Crie uma tupla com as letras do alfabeto e uma segunda tupla com as vogais.
Imprima a diferença entre as duas tuplas.
'''

print("-------------- Alfabeto -------------- ")

alfabeto = tuple("abcdefghijklmnopqrstuvwxyz")
print(alfabeto)
vogais = ("a", "e", "i", "o", "u")
print(vogais)

conjunto_alfabeto = set(alfabeto)
conjunto_vogais = set(vogais)

diferenca = conjunto_alfabeto - conjunto_vogais

print("Diferença entre as duas tuplas:", diferenca)
print("--------------------------------------")