exerci3 = [7.5, 8.5, 9.0, 10]
media = 0
for i in range(0, len(exerci3)):
    print("nota", i+1, ":", exerci3[i])
    media = media + exerci3[i]
media = media / len(exerci3)
print("Média:", media)
