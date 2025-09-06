#1 -

comprimento = int(input("Digite o comprimento do terreno (em metros): "))
largura = int(input("Digite a largura do terreno (em metros): "))
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}")

#2-

fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

celsius = (fahrenheit - 32) * (5 / 9)

celsius_inteiro = int(celsius)

print(f"{fahrenheit} graus Fahrenheit são {celsius_inteiro} graus Celsius.")

#3-

produto1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
quantidade1 = int(input("Digite a quantidade do produto 1:"))

produto2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
quantidade2 = int(input("Digite a quantidade do produto 2:"))

produto3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
quantidade3 = int(input("Digite a quantidade do produto 3:"))

total = (p  reco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)

print(f"Total: R${total:,.2f}")

#4-

# Lê o valor inteiro em reais
valor = int(input())

# Lista das notas disponíveis em ordem decrescente
notas = [100, 50, 20, 10, 5, 2, 1]

# Para cada nota, calcula quantas são necessárias e atualiza o valor restante
for nota in notas:
    quantidade = valor // nota  # Quantidade de notas do valor atual
    valor = valor % nota        # Atualiza o valor restante
    print(f"{quantidade} nota(s) de R${nota},00")

