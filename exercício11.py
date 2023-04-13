vetor1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
vetor2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
vetor3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
vetor4 = []

contador = 0
for i in vetor1:
    vetor4.append(i)
    vetor4.append (vetor2[contador])
    vetor4.append (vetor3[contador])
    contador += 1
print ("Números intercalados entre os vetores:")
print(vetor4)