'''
6. Crie um conjunto com as cores do arco-íris (vermelho, laranja, amarelo, verde,
azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor
digitada está no conjunto e imprima uma mensagem correspondente.
'''

cores = {"vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta"}
cores2 = {"Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta"}

print("--------------- Cores do Arco-íris ---------------")

corDigitada = input("Digite uma cor: ")

if corDigitada in cores:
    print(f"A cor {corDigitada} faz parte das cores do arco-íris.")
else:
    print(f"A cor {corDigitada} não é uma cor do arco-íris.")

print("--------------------------------------------------")