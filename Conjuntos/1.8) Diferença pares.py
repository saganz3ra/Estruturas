'''
8. Crie um conjunto com os números de 1 a 20 e outro conjunto com os
números pares de 1 a 10. Imprima a diferença entre os dois conjuntos.
'''

print("---------- CONJUNTOS ----------")
pares = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
pares2 = {2, 4, 6, 8, 10}

print("O conjunto 1 é: 2, 4, 6, 8, 10")
print("O conjunto 2 é: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20")
print("-------------------------------")

diferenca = pares.difference(pares2)
print("A diferença dos conjuntos pares 1 e 2 é:")
print(diferenca)
print("-------------------------------")