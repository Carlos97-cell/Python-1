idade = int(input("Digite sua idade: "))
jogou_tres_ou_mais = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False): ") == "True"
vitorias = int(input("Quantas vezes você venceu um jogo de tabuleiro? "))

pode_entrar = (16 <= idade <= 18) and jogou_tres_ou_mais and (vitorias >= 1)

print(pode_entrar)
