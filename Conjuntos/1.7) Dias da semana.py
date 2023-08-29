'''
7. Crie um conjunto com os dias da semana (segunda, terça, quarta, quinta,
sexta, sábado, domingo) e remova os dias úteis (segunda a sexta). Imprima o
conjunto resultante.
'''

semana = {"segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"}

print("---------- Dias da Semana ----------")
semana.remove("segunda")
semana.remove("sexta")

print(semana)
print("------------------------------------")