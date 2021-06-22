import locale

locale.setlocale( locale.LC_ALL, '' )

def aposta(quantidade_dezenas):
    while(True):
        if quantidade_dezenas == 6:
            print (locale)
            valor_para_pagar = 4.50
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 7:
            valor_para_pagar = 31.50
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 8:
            valor_para_pagar = 126.00
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 9:
            valor_para_pagar = 378.00
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 10:
            valor_para_pagar = 945.00
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 11:
            valor_para_pagar = 2079.00
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 12:
            valor_para_pagar = 4158.00
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 13:
            valor_para_pagar = 7722.00
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 14:
            valor_para_pagar = 13513.50
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
        if quantidade_dezenas == 15:
            valor_para_pagar = 22522.50
            converter_moeda = locale.currency( valor_para_pagar, grouping=True )
            print(f"O valor total à pagar na aposta é de {converter_moeda}")
            return converter_moeda
    else:
        print ("Não foram encontrado valores para a quantidade de dezenas informadas")


if __name__ == "__main__":
    aposta(15)