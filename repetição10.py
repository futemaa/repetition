
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))


if numero1 < numero2:
    menor = numero1
    maior = numero2
else:
    menor = numero2
    maior = numero1


for i in range(menor, maior+1):
    print(i)



