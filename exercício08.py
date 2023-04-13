idade = [90, 40, 33, 21, 56]
altura = [1.78, 1.5, 1.90, 1.3, 1.69]
alturaVazia = []
idadeVazia = []

for i in range(5):
    idadeVazia.append(idade.pop())
    alturaVazia.append(altura.pop())

print(idadeVazia)
print(alturaVazia)