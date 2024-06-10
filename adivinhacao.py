import random


def jogo_de_adivinhacao():
    tentativas = 5
    senha = random.randrange(1, 101)
    print(senha)

    try:
        while tentativas > 0:
            palpite = int(input("Escolha um número de 1 a 100: "))
            if palpite > 100 or palpite < 0:
                print("Número inválido. Tente novamente.")
            else:
                if palpite > senha:
                    tentativas -= 1
                    print(
                        f"Você errou! O número secreto é menor. \nRestam *{tentativas}* tentativas.")
                elif palpite < senha:
                    tentativas -= 1
                    print(
                        f"Você errou! O número secreto é maior. \nRestam *{tentativas}* tentativas.")
                elif palpite == senha:
                    tentativas -= 1
                    print(f"Você acertou!! Foram feitas {
                          5 - tentativas} tentativas. O número secreto é ** {senha} **.")
                    break
        else:
            print(
                f"Acabaram as tentativas... O número secreto era ** {senha} **.")

        nova_rodada = int(input("""Novo jogo? 
            [1] - Sim
            [2] - Não
            >> """))
        if nova_rodada == 1:
            jogo_de_adivinhacao()
        else:
            print("Saindo...")

    except ValueError:
        print("Valor inválido. Programa encerrado.")


print(f"{"*" * 5} JOGO DE ADIVINHAÇÃO {"*" * 5}")
jogo_de_adivinhacao()
