import locale

locale.setlocale( locale.LC_ALL, '' )

VALOR = {
    6: (4.50),
    7: (31.50),
    8: (126.00),
    9: (378.00),
    10: (945.00),
    11: (2079.00),
    12: (4158.00),
    13: (7722.00),
    14: (13513.50),
    15: (22522.50)
}


def aposta(quantidade_dezenas):
    while (True):
        if quantidade_dezenas in VALOR:
            valor_aposta = locale.currency(VALOR.get(quantidade_dezenas), grouping=True )
            print(f"O valor total à pagar na aposta é de {valor_aposta}")
            return valor_aposta
        else:
            print ("Não foram encontrado valores para a quantidade de dezenas informadas")
            break


if __name__ == "__main__":
    aposta(15)