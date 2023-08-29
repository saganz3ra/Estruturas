''' 
2. Crie dois conjuntos, um com os números de 1 a 5 e outro com os números de
3 a 7. Imprima a união, a interseção e a diferença simétrica dos conjuntos.   
'''
print("---------- CONJUNTOS ----------")
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
print("O conjunto 1 é: 1, 2, 3, 4 e 5")
print("O conjunto 2 é: 3, 4, 5, 6 e 7")
print("-------------------------------")

uniao = conjunto.union(conjunto2)
print("A união do conjunto 1 com o 2 é:")
print(uniao)
print("-------------------------------")

interseccao = conjunto.intersection(conjunto2)
print("A intersecção do conjunto 1 com o 2 é:")
print(interseccao)
print("-------------------------------")

diferenca = conjunto.difference(conjunto2)
print("A diferença simétrica dos conjuntos 1 e 2 é:")
print(diferenca)
print("-------------------------------")