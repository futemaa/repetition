populacao_A = 80000
taxa_crescimento_A = 0.03

populacao_B = 200000
taxa_crescimento_B = 0.015

anos = 0

while populacao_A < populacao_B:
    anos += 1
    populacao_A += int(populacao_A * taxa_crescimento_A)
    populacao_B += int(populacao_B * taxa_crescimento_B)

print(f"Serão necessários {anos} anos para que a população de A iguale ou ultrapasse a população de B.")