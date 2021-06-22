import random


def sortear_dezenas():
    random.seed()
    numeros_sorteados = random.sample(range(1,60), 6) # Definindo e sorteando números entre 1 e 60 com 6 sorteios
    while len(numeros_sorteados) != 6: # enquanto não preencher o array com os 6 sorteios
        numero_sorteado = random.randint() # sortear número, não precisa definir range pois já foi definido no sample
        if numero_sorteado not in numeros_sorteados: # Verifica se o número sorteado já está dentro do array 
            numeros_sorteados.append(numero_sorteado)
    numeros_sorteados_ordenados = sorted(numeros_sorteados) # Faz a ordenação dos números sorteados de números sorteados
    # print(f"As dezenas sorteadas foram {numeros_sorteados_ordenados}")
    return numeros_sorteados_ordenados # Faz o retorno do sorteio realizado, quando a função for chamada


if __name__ == "__main__":
    sortear_dezenas()