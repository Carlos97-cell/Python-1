# Solicita os dados do usuário
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

# Define o valor base por kg conforme a distância
if distancia <= 100:
    valor_por_kg = 1.00
elif distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

# Calcula o valor do frete
frete = peso * valor_por_kg

# Aplica taxa extra para pacotes acima de 10 kg
if peso > 10:
    frete += 10.00

# Exibe o valor final do frete
print(f"Valor do frete: R${frete:.2f}")