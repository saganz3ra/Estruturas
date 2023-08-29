'''
9. Crie um conjunto com as notas de um aluno em uma disciplina e verifique se
ele foi aprovado (média 7) ou reprovado (média abaixo de 7).
'''

def aprovacao(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

print("--------------- NOTAS -----------------")
notas = {8, 7.5, 6, 9, 5.5}
print("Suas notas foram: 8, 7.5, 6, 9, 5.5")

resultado = aprovacao(notas)
print("Resultado:", resultado)
print("---------------------------------------")