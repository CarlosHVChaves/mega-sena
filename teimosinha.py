from jogo import escolher_dezenas
from sorteio import sortear_dezenas


def teimosinha():
    sorteios_realizados = []
    acertos_realizados = []
    acertos_jogo = []
    jogo = escolher_dezenas()
    while (True):
        quantidade_jogos = int(input ("Informe a quantidade de vezes que você irá usar esse jogo (opções: 2, 4 ou 8 sorteios)"))
        if (quantidade_jogos == 2) or (quantidade_jogos == 4) or (quantidade_jogos == 8):
            print (f"Quantidade de sorteios que seu jogo irá participar: {quantidade_jogos}")
            for x in range(quantidade_jogos):
                sorteio = sortear_dezenas()
                print (f"No {x+1}º sorteio, o sistema sorteou as seguintes dezenas: {sorteio}")
                sorteios_realizados.append(sorteio)
            print (f"TEIMOSINHA: Relação completa dos sorteios feitos {sorteios_realizados}")
            print (len(sorteios_realizados[0]))
            for x in range(len(sorteios_realizados)):
                for y in range(len(jogo)):
                    if jogo[y] in sorteios_realizados[x]:
                        acertos_realizados.append(jogo[y])
                acertos_jogo.append(acertos_realizados)
                acertos_realizados = []
            for x in range(len(acertos_jogo)):
                print (f"No {x+1}º sorteio foram acertadas {len(acertos_jogo[x])} dezenas, e elas foram:{acertos_jogo[x]}")
            print (f"TEIMOSINHA: As dezenas acertadas de cada sorteio foram: {acertos_jogo}")
            return acertos_jogo
        else:
            print ("Quantidade informada não atende aos requisitos do jogo")


if __name__ == "__main__":
    teimosinha()