'''
6. Crie uma tupla com as cores do arco-íris (vermelho, laranja, amarelo, verde,
azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
digitada está na tupla e imprima uma mensagem correspondente.
'''

print("-------------------- Cores do Arco Íris --------------------")

cores= ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta")

cor_digitada = input("Digite uma cor: ")

if cor_digitada in cores:
    print("A cor", cor_digitada, "está no arco-íris!")
else:
    print("A cor", cor_digitada, "não faz parte do arco-íris.")

print("------------------------------------------------------------")