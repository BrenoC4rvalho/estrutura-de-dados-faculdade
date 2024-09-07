""" 

definição:  um algoritmo de ordenação simples que divide a lista em duas partes: a parte ordenada e a parte
não ordenada. O algoritmo trabalha selecionando repetidamente o menor (ou maior, dependendo da ordem desejada)
elemento da parte não ordenada e movendo-o para a parte ordenada.

comportamento:  Comece no início da lista e considere toda a lista como não ordenada.
                Encontre o menor elemento na parte não ordenada da lista.
                Troque o menor elemento encontrado com o primeiro elemento da parte não ordenada, 
movendo-o para a parte ordenada.
                Mova o limite entre as partes ordenada e não ordenada uma posição à frente.
                Repita o processo para o restante da lista até que toda a lista esteja ordenada. 

complexidade de tempo: O(n²)

"""

def main(x):
    w = 0  # Contador para a quantidade de vezes em que o laço mais externo é executado (trocas)
    n = len(x)  # Tamanho da lista

    # Laço externo que percorre todos os elementos da lista, exceto o último
    for i in range(0, n - 1):
        # Laço interno que compara o elemento atual com todos os elementos subsequentes
        for j in range(i + 1, n):
            w = w + 1  # Incrementa a quantidade de comparações realizadas

            # Se o elemento atual for maior que o elemento subsequente, troca-os de lugar
            if x[i] > x[j]:
                # Realiza a troca dos elementos
                z = x[i]  # Armazena o valor de x[i] em uma variável temporária
                x[i] = x[j]  # Coloca o valor de x[j] em x[i]
                x[j] = z  # Coloca o valor armazenado em z (original x[i]) em x[j]

    # Exibe a quantidade total de comparações realizadas durante o algoritmo
    print(f'Quantidade de trocas foi {w} vezes no selection sort')
