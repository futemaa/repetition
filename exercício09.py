A = []

for i in range (10):
    numero = int(input(f"Digite o {i+1}º numero:"))
    A.append(numero)

soma = sum(A)
multiplicação = 1
for numero in A:
    multiplicação *= numero
print ("soma dos numeros:")
print (soma)
print ("numero da soma ao quadrado:")
print (multiplicação)