'''
4. Crie dois conjuntos com nomes de frutas e verifique se há alguma fruta em
comum entre os conjuntos.
'''

frutas = {'Maça', 'Mangostão', 'Pêra', 'Acerola', 'Caqui', 'Jaca'}
frutas2 = {'Caqui', 'Pêra', 'Banana', 'Limão', 'Pitaia', 'Laranja', 'Uva', 'Mangostão', 'Jaca'}

print("------------ FRUTAS -----------")
interseccao = frutas.intersection(frutas2)

print("As frutas comuns entre os conjuntos são: ")
print(interseccao)
print("-------------------------------")