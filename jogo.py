def escolher_quantidade_dezenas():
    while (True):
        quantidades_dezenas = int(input ("Informe a quantidade de dezenas que será inserida no seu jogo (mínimo 6 - máximo 15)"))
        if (quantidades_dezenas < 6) or (quantidades_dezenas > 15):
            print ("Quantidade informada não atende aos requisitos do jogo")
        else:
            print (f"Quantidade de dezenas que serão informadas: {quantidades_dezenas}")
        return quantidades_dezenas


def escolher_dezenas():
    quantidade_dezenas = escolher_quantidade_dezenas()
    numeros_escolhidos = []
    while len(numeros_escolhidos) < (quantidade_dezenas):
        escolha_dezena = int(input (f"Informe a {int(len(numeros_escolhidos)+1)}ª dezena (mínimo 1 - máximo 60)"))
        if escolha_dezena not in numeros_escolhidos: # Verifica se o número escolhido já está dentro do array
            if (escolha_dezena >= 1) and (escolha_dezena <= 60):
                numeros_escolhidos.append(escolha_dezena)
            else:
                print ("Dezena informada não atende aos requisitos do jogo")
        else:
            print ("Dezena informada já foi inserida anteriormente")
    numeros_escolhidos_ordenados = sorted(numeros_escolhidos)
    print(f"As dezenas escolhidas foram {numeros_escolhidos_ordenados}")
    return numeros_escolhidos_ordenados
    


if __name__ == "__main__":
    escolher_dezenas()