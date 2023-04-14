while True:
    try:
        populacao_A = int(input("Digite a população inicial do país A: "))
        taxa_crescimento_A = float(input("Digite a taxa de crescimento anual do país A em porcentagem (exemplo: 3 para 3%): ")) / 100
        populacao_B = int(input("Digite a população inicial do país B: "))
        taxa_crescimento_B = float(input("Digite a taxa de crescimento anual do país B em porcentagem (exemplo: 1.5 para 1.5%): ")) / 100
        if populacao_A > 0 and populacao_B > 0 and taxa_crescimento_A > 0 and taxa_crescimento_B > 0:
            break
        else:
            print("Os valores devem ser maiores que zero.")
    except ValueError:
        print("Valores inválidos. Digite novamente.")

anos = 0

while populacao_A < populacao_B:
    anos += 1
    populacao_A += int(populacao_A * taxa_crescimento_A)
    populacao_B += int(populacao_B * taxa_crescimento_B)

print(f"Serão necessários {anos} anos para que a população de A iguale ou ultrapasse a população de B.")