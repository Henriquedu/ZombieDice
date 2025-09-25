#!/usr/bin/env python3
# Zombie Dice - versão terminal
# Regras principais:
# - 13 dados no saco: 6 verdes, 4 amarelos, 3 vermelhos
# - Faces por cor:
#   Green: 3 brains, 2 footprints, 1 shotgun
#   Yellow: 2 brains, 2 footprints, 2 shotguns
#   Red: 1 brain, 2 footprints, 3 shotguns
# - Em cada jogada o jogador puxa 3 dados (repondo footprint para próxima rolagem).
# - Se o jogador acumular 3 shotguns na mesma rodada, ele perde os cérebros acumulados na rodada.
# - Quando algum jogador atinge a pontuação alvo (default 13), completa-se a rodada para todos e quem tiver mais brains vence.

import random
# === CONFIGURAÇÕES DO JOGO ===
TARGET = 13  # Pontuação para vencer

# Dados (cor + faces)
DICE = [
    ("green",    ["brain", "brain", "brain", "footprint", "footprint", "shotgun"]),
    ("green",    ["brain", "brain", "brain", "footprint", "footprint", "shotgun"]),
    ("green",    ["brain", "brain", "brain", "footprint", "footprint", "shotgun"]),
    ("green",    ["brain", "brain", "brain", "footprint", "footprint", "shotgun"]),
    ("green",    ["brain", "brain", "brain", "footprint", "footprint", "shotgun"]),
    ("yellow",   ["brain", "brain", "footprint", "footprint", "shotgun", "shotgun"]),
    ("yellow",   ["brain", "brain", "footprint", "footprint", "shotgun", "shotgun"]),
    ("yellow",   ["brain", "brain", "footprint", "footprint", "shotgun", "shotgun"]),
    ("yellow",   ["brain", "brain", "footprint", "footprint", "shotgun", "shotgun"]),
    ("red",      ["brain", "footprint", "footprint", "shotgun", "shotgun", "shotgun"]),
    ("red",      ["brain", "footprint", "footprint", "shotgun", "shotgun", "shotgun"]),
    ("red",      ["brain", "footprint", "footprint", "shotgun", "shotgun", "shotgun"]),
]

# === FUNÇÕES DO JOGO ===

def draw_dice(bag, num):
    random.shuffle(bag)
    draw = []
    while len(draw) < num and bag:
        draw.append(bag.pop())
    return draw

def roll_die(die):
    color, faces = die
    return color, random.choice(faces)

def play_round():
    bag = DICE.copy()
    footprints = []
    round_brains = 0
    round_shotguns = 0

    while True:
        needed = 3 - len(footprints)
        drawn = draw_dice(bag, needed)
        hand = footprints + drawn
        footprints = []

        if not hand:
            print("⚠️ Não há mais dados no saco.")
            break

        print("\nRolando os dados...")
        for d in hand:
            color, face = roll_die(d)
            print(f"{color.upper()} -> {face}", end=" | ")
            if face == "brain":
                round_brains += 1
            elif face == "shotgun":
                round_shotguns += 1
            else:
                footprints.append(d)
        print(f"\nCérebros acumulados: {round_brains}, Tiros recebidos: {round_shotguns}")

        if round_shotguns >= 3:
            print("💥 Você levou 3 tiros! Perdeu todos os cérebros desta rodada.")
            return 0

        escolha = input("Deseja rolar novamente? (s/n): ").lower()
        if escolha != "s":
            print(f"Você parou com {round_brains} cérebros nesta rodada.")
            return round_brains

def main():
    print("=== Zombie Dice === 🧟🎲")
    jogadores = []
    n = int(input("Quantos jogadores? "))

    for i in range(n):
        nome = input(f"Nome do jogador {i+1}: ")
        jogadores.append(nome)

    pontuacoes = {j: 0 for j in jogadores}
    final = False

    while True:
        for jogador in jogadores:
            print(f"\n--- Vez de {jogador} ---")
            print(f"Pontuação atual: {pontuacoes[jogador]} cérebros")
            ganho = play_round()
            pontuacoes[jogador] += ganho
            print(f"{jogador} agora tem {pontuacoes[jogador]} cérebros.\n")

            if pontuacoes[jogador] >= TARGET:
                final = True
        if final:
            vencedor = max(pontuacoes, key=lambda x: pontuacoes[x])
            print("🏆 FIM DE JOGO!")
            print(f"O vencedor foi {vencedor} com {pontuacoes[vencedor]} cérebros!")
            break

# Executar o jogo
if __name__ == "__main__":
    main()
