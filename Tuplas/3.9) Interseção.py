'''
9. Crie uma tupla com os números de 1 a 10 e outra tupla com os números de 5
a 15. Imprima a interseção entre as duas tuplas.
'''

print("------------------------ Números ------------------------")

numeros = tuple(range(1, 11))  # Números de 1 a 10
numeros2 = tuple(range(5, 16))  # Números de 5 a 15

conjunto = set(numeros)
conjunto2 = set(numeros2)

intersecao = conjunto & conjunto2

print("Interseção entre as duas tuplas:", intersecao)

print("---------------------------------------------------------")