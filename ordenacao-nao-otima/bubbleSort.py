""" 

definição: é um algoritmo de ordenação simples que repete várias vezes pela lista,
comparando elementos adjacentes e os trocando se estiverem na ordem errada. O processo
continua até que a lista esteja ordenada

comportamento:  Comece no início da lista e compare o primeiro par de elementos adjacentes.
                Se o primeiro elemento for maior que o segundo, troque-os de lugar.
                Mova para o próximo par de elementos adjacentes e repita o processo.
                Após uma passagem completa pela lista, o maior elemento "bolha" para o final.
                Repita o processo para a lista restante, ignorando o último elemento já ordenado.
                Continue repetindo até que não sejam necessárias mais trocas, o que significa que a lista está ordenada.

complexidade de tempo: O(n²)

"""

def main(x):
    w = 0  # Contador para a quantidade de comparações realizadas
    n = len(x)  # Obtém o tamanho da lista

    # Loop externo: percorre a lista até o penúltimo elemento
    for j in range(0, n - 1):
        # Loop interno: compara e possivelmente troca os elementos restantes
        for i in range(n - 1, j, -1):
            w = w + 1  # Incrementa a quantidade de comparações

            # Se o elemento anterior é maior que o elemento atual
            if x[i - 1] > x[i]:
                # Troca os elementos x[i - 1] e x[i]
                z = x[i]  # Armazena temporariamente o valor de x[i]
                x[i] = x[i - 1]  # Move o valor de x[i - 1] para x[i]
                x[i - 1] = z  # Move o valor armazenado em z para x[i - 1]
    
    # Opcional: imprime a quantidade de comparações realizadas
    print(f'Quantidade de comparações foi {w} vezes no bubble sort')

    print(f'Quantidade de trocas foi {w} vezes no bubble sort')
