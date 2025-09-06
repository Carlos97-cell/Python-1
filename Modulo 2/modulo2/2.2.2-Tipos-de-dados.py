#Armazene o texto "o resultado é"  em uma variável, o valor 10 em outra variável, e o valor 3.5 numa terceira variável.

#Some os valores da segunda e terceira variável e armazene em outra variável.

#Imprima todas as variáveis na ordem de criação e imprima também seus tipos.

#1
texto = "o resultado é"
valor_1 = 10
valor_2 = 3.5


resultado = valor_1 + valor_2

print(texto)
print(type(texto))

print(valor_1)
print(type(valor_2))

print("valor_decimal")
print(type("valor_decimal"))

print(resultado)
print(type(resultado))

#2
# Armazenando os valores
texto = "o resultado é"
num1 = 10
num2 = 3.5

# Somando os números
soma = num1 + num2

# Imprimindo variáveis e seus tipos
print(texto)
print(type(texto))

print(num1)
print(type(num1))

print(num2)
print(type(num2))

print(soma)
print(type(soma))

#3
v1 = 10
v2 = 20

aux = v1
v1 = v2
v2 = aux

print(v1)  # 20
print(v2)  # 10

#4
saldo = 500.0
juros = 1.01

saldo = saldo * juros
saldo = saldo * juros
saldo = saldo * juros

print("Após 3 meses meu novo saldo é")
print(saldo)