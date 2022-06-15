from random import shuffle, choice
from collections import namedtuple
import time


def criar_dados():
    Dado = namedtuple("Dado", ['cor', 'lados'])
    dado_verde = Dado('verde', ['cerebro', 'cerebro', 'cerebro', 'passo', 'passo', 'tiro'])
    dado_vermelho = Dado('vermelho', ['cerebro', 'passo', 'passo', 'tiro', 'tiro', 'tiro'])
    dado_amarelo = Dado('amarelo', ['cerebro', 'cerebro', 'passo', 'passo', 'tiro', 'tiro'])

    # Populando lista de dados
    lista_dados = []
    for _ in range(6):
        lista_dados.append(dado_verde)
    for _ in range(3):
        lista_dados.append(dado_vermelho)
    for _ in range(4):
        lista_dados.append(dado_amarelo)

    shuffle(lista_dados)
    return lista_dados


def criar_jogadores():
    jogadores = []

    while True:
        try:
            num_jogadores = int(input("Digite quantos jogadores irão jogar: "))
            if num_jogadores > 1:
                break
            else:
                print("Você precisa de no mínimo dois jogadores para jogar!")
        except ValueError:
            print("O número precisa ser um inteiro.")

    for i in range(num_jogadores):
        nome = input(f"Digite o nome do jogador {i+1}: ").capitalize()
        jogador = {'nome': nome, 'pontuacao': 0}
        jogadores.append(jogador)

    shuffle(jogadores)
    print("*** ORDEM PARA JOGAR ***")
    n = 1
    for jogador in jogadores:
        print(f"{n}. {jogador['nome']}")
        n += 1

    return jogadores


def turno(jogador):
    print(f"\nVez do jogador {jogador['nome']}")
    time.sleep(0.5)

    lista_dados = criar_dados()
    pontuacao_temp = {'cerebros': 0, 'tiros': 0}
    dados_na_mao = []

    while True:
        while len(dados_na_mao) < 3:
            dados_na_mao.append(lista_dados.pop())

        n = 1
        for dado in reversed(dados_na_mao):
            time.sleep(0.3)
            print(f"Jogando dado {n}")
            n += 1

            cor = dado.cor
            shuffle(dado.lados)
            lado_sorteado = choice(dado.lados)

            print(f"   Cor: {cor}\n   Lado: {lado_sorteado}")

            # Verificando dados
            if lado_sorteado == 'cerebro':
                pontuacao_temp['cerebros'] += 1
                lista_dados.append(dados_na_mao.pop(dados_na_mao.index(dado)))
            elif lado_sorteado == 'tiro':
                pontuacao_temp['tiros'] += 1
                lista_dados.append(dados_na_mao.pop(dados_na_mao.index(dado)))
            shuffle(lista_dados)

        print(f"\nCérebros atuais: {pontuacao_temp['cerebros']}\nTiros atuais: {pontuacao_temp['tiros']}")
        if pontuacao_temp['tiros'] < 3:
            if input("\nDeseja continuar jogando? (s/n): ").upper() != 'S':
                print(f"Você conseguiu {pontuacao_temp['cerebros']} cérebros.")
                jogador['pontuacao'] += pontuacao_temp['cerebros']
                break
        else:
            print(f"Você tomou muitos tiros e acabou perdendo {pontuacao_temp['cerebros']} cérebros.")
            break


def placar(jogadores):
    print("\n*** PLACAR ATUAL ***")
    for jogador in jogadores:
        print(f"{jogador['nome']}: {jogador['pontuacao']} pontos.")


jogadores = criar_jogadores()

game_over = False
while not game_over:
    for jogador in jogadores:
        turno(jogador)
        if jogador['pontuacao'] >= 13:
            vencedor = jogador['nome']
            game_over = True
    if not game_over:
        placar(jogadores)
    else:
        print(f"\nO jogo acabou. O grande vencedor foi: {vencedor}.")
        placar(jogadores)
