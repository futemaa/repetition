while True:
    nome = input("Digite o nome: ")
    if len(nome) > 3:
        break
    print("Nome inválido! O nome deve ter mais de 3 caracteres.")

while True:
    idade = int(input("Digite a idade: "))
    if idade >= 0 and idade <= 150:
        break
    print("Idade inválida! A idade deve estar entre 0 e 150 anos.")

while True:
    salario = float(input("Digite o salário: "))
    if salario > 0:
        break
    print("Salário inválido! O salário deve ser maior que zero.")

while True:
    sexo = input("Digite o sexo (f/m): ")
    if sexo in ('f', 'm'):
        break
    print("Sexo inválido! O sexo deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite o estado civil (s/c/v/d): ")
    if estado_civil in ('s', 'c', 'v', 'd'):
        break
    print("Estado civil inválido! O estado civil deve ser 's', 'c', 'v' ou 'd'.")

print("Cadastro realizado!")