jogador1 = input("Digite o nome do primeiro jogador: ")
gols1 = int(input(f"Digite o número de gols de {jogador1}: "))
assistencias1 = int(input(f"Digite o número de assistências de {jogador1}: "))
jogos1 = int(input(f"Digite o número de jogos de {jogador1}: "))



jogador2 = input("Digite o nome do segundo jogador: ")
gols2 = int(input(f"Digite o número de gols de {jogador2}: "))
assistencias2 = int(input(f"Digite o número de assistências de {jogador2}: "))
jogos2 = int(input(f"Digite o número de jogos de {jogador2}: "))

# Comparação dos jogadores/GOLS/ASSSISTÊNCIAS/JOGOS

print(f"\n ======= COMPARAÇÃO DOS JOGADORES {jogador1} e {jogador2} =======")
print(f"{jogador1} marcou {gols1} gols.")
print(f"{jogador2} marcou {gols2} gols.")
print(f"{jogador1} fez {assistencias1} assistências.")
print(f"{jogador2} fez {assistencias2} assistências.")
print(f"{jogador1} jogou {jogos1} partidas.")
print(f"{jogador2} jogou {jogos2} partidas.")

# Cálculo da média de gols por partida

media1 = gols1 / jogos1
media2 = gols2 / jogos2

print(f"\nA média de gols por partida de {jogador1} é: {media1:.2f}")
print(f"A média de gols por partida de {jogador2} é: {media2:.2f}")

# Cálculo da média de assistências por partida

media_assistencias1 = assistencias1 / jogos1
media_assistencias2 = assistencias2 / jogos2


print(f"\nA média de assistências por partida de {jogador1} é: {media_assistencias1:.2f}")
print(f"A média de assistências por partida de {jogador2} é: {media_assistencias2:.2f}")

# logica de quem marcou mais gols

if gols1 > gols2:
    print(f"\nO jogador {jogador1} marcou mais gols que {jogador2}.{gols1} > {gols2}")
elif gols2 > gols1:
    print(f"\nO jogador {jogador2} marcou mais gols que {jogador1}. {gols2} > {gols1}")
else:
    print(f"\nOs jogadores {jogador1} e {jogador2} empataram no numero de gols.")

# logica de media de gols por partida

if media1 > media2:
    print(f"\nO jogador {jogador1} tem uma média de gols por partida maior que {jogador2}. {media1:.2f} > {media2:.2f}")
elif media2 > media1:
    print(f"\nO jogador {jogador2} tem uma média de gols por partida maior que {jogador1}. {media2:.2f} > {media1:.2f}")
else:
    print(f"\nOs jogadores {jogador1} e {jogador2} empataram na média de gols por partida.{media1:.2f} = {media2:.2f}")

# logica de media de assistencias por partida

if media_assistencias1 > media_assistencias2:
    print(f"\nO jogador {jogador1} tem uma média de assistências por partida maior que {jogador2}. {media_assistencias1:.2f} > {media_assistencias2:.2f}")
elif media_assistencias2 > media_assistencias1:
    print(f"\nO jogador {jogador2} tem uma média de assistências por partida maior que {jogador1}. {media_assistencias2:.2f} > {media_assistencias1:.2f}")
else:
    print(f"\nOs jogadores {jogador1} e {jogador2} empataram na média de assistências por partida.{media_assistencias1:.2f} = {media_assistencias2:.2f}")

# logica de participacoes em gols (gols + assistencias) por partida

participacoes1 = gols1 + assistencias1
participacoes2 = gols2 + assistencias2

media_participacoes1 = participacoes1 / jogos1
media_participacoes2 = participacoes2 / jogos2

if media_participacoes1 > media_participacoes2:
    print(f"\nO jogador {jogador1} tem uma média de participações em gols por partida maior que {jogador2}. {media_participacoes1:.2f} > {media_participacoes2:.2f}")
elif media_participacoes2 > media_participacoes1:
    print(f"\nO jogador {jogador2} tem uma média de participações em gols por partida maior que {jogador1}. {media_participacoes2:.2f} > {media_participacoes1:.2f}")
else:
    print(f"\nOs jogadores {jogador1} e {jogador2} empataram na média de participações em gols por partida.{media_participacoes1:.2f} = {media_participacoes2:.2f}")

# relatorio ofensivo final, gols + assistencias + jogos + media de gols + media de assistencias + media de participacoes

print(f"\n ======= RELATÓRIO OFENSIVO FINAL =======")

def relatorio_ofensivo(jogador, gols, assistencias, jogos, media_gols, media_assistencias, media_participacoes):
    print(f"\nJogador: {jogador}")
    print(f"Gols: {gols}")
    print(f"Assistências: {assistencias}")
    print(f"Jogos: {jogos}")
    print(f"Média de gols por partida: {media_gols:.2f}")
    print(f"Média de assistências por partida: {media_assistencias:.2f}")
    print(f"Média de participações em gols por partida: {media_participacoes:.2f}")

relatorio_ofensivo(jogador1, gols1, assistencias1, jogos1, media1, media_assistencias1, media_participacoes1)
relatorio_ofensivo(jogador2, gols2, assistencias2, jogos2, media2, media_assistencias2, media_participacoes2)