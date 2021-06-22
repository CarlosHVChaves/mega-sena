from sorteio import sortear_dezenas


def surpresinha():
    jogos = []
    while (True):
        quantidade_jogos = int(input ("Informe a quantidade de jogos que deseja que o sistema faça por você (mínimo 1 - máximo 8)"))
        if (quantidade_jogos < 1) or (quantidade_jogos > 8):
            print ("Quantidade informada não atende aos requisitos do jogo")
        else:
            print (f"Quantidade de jogos que serão feitos pelo sistema: {quantidade_jogos}")
            for x in range(quantidade_jogos):
                dezenas_escolhidas_sistema = sortear_dezenas()
                print (f"No {x+1}º jogo, o sistema escolheu as seguintes dezenas: {dezenas_escolhidas_sistema}")
                jogos.append(dezenas_escolhidas_sistema)
            print (f"SURPRESINHA: Relação completa dos jogos feitos pelo sistema {jogos}") # Para pegar apenas um dos arrays, é só usar o colchetes, exemplo: jogos[0] onde zero é a primeita posição do array de jogos
            return jogos


if __name__ == "__main__":
    surpresinha()