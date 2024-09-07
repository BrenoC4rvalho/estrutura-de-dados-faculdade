""" 

definição: é um algoritmo de ordenação simples que constrói a lista final ordenada um item de cada vez. 
Ele funciona de maneira semelhante à forma como muitas pessoas ordenam cartas em suas mãos: inserindo cada 
carta na posição correta, uma por vez, de forma crescente.

comportamento:  Iteração Inicial: O algoritmo começa com o segundo elemento da lista (índice 1), 
assumindo que o primeiro elemento está em sua posição correta.
                Comparação e Deslocamento:
                    Para cada elemento a partir do segundo até o final da lista, o algoritmo o compara com os 
elementos anteriores que já estão ordenados.
                    Enquanto o elemento corrente (v) for menor que o elemento anterior, ele desloca o elemento 
anterior uma posição à frente.
                Inserção: Depois de deslocar os elementos maiores, insere o elemento corrente na posição correta.
                Repetição: Repete o processo para todos os elementos da lista até que toda a lista esteja ordenada.

complexidade de tempo: O(n²)

"""

def main(x):
    w = 0  # Quantidade de trocas realizadas
    n = len(x)  # Tamanho da lista
    
    # Começa a partir do segundo elemento
    for i in range(1, n):
        v = x[i]  # O valor corrente a ser inserido
        j = i  # Índice do valor corrente
        
        # Move os elementos maiores que v para uma posição à frente
        while j > 0 and x[j - 1] > v:
            w = w + 1  # Incrementa a contagem de trocas
            x[j] = x[j - 1]  # Move o elemento maior para a posição à frente
            j = j - 1  # Move o índice para a esquerda
        
        # Insere o valor corrente na posição correta
        x[j] = v
    
    # Imprime a quantidade de trocas realizadas
    print(f'Quantidade de trocas foi {w} vezes no insertion sort')
