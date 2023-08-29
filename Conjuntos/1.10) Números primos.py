'''
10. Crie um conjunto com os números primos de 1 a 20 e verifique se um número
digitado pelo usuário está no conjunto.
'''

primos = {2, 3, 5, 7, 11, 13, 17, 19}

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

print("---------- Números Primos ----------")

numero_digitado = int(input("Digite um número: "))


if numero_digitado in primos:
    print(f"{numero_digitado} é um número primo.")
else:
    print(f"{numero_digitado} não é um número primo.")

print("------------------------------------")