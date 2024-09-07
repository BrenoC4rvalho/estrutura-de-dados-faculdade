""" 

definição: é um algoritmo de ordenação que generaliza o Insertion Sort para aumentar sua eficiência, especialmente 
em listas maiores. Ele funciona dividindo a lista em sublistas, baseando-se em um intervalo ou "gap", e ordenando 
essas sublistas. Com o tempo, o intervalo é reduzido até que a lista inteira seja processada com um intervalo de 1
(o que equivale ao Insertion Sort).
O algoritmo que você forneceu usa a sequência de Knuth para definir os gaps. A sequência é calculada como h = h * 3 + 1, 
e o algoritmo começa com o maior gap menor que o tamanho da lista e, gradualmente, o reduz até que h = 1.

comportamento:  Inicialização do Gap: O algoritmo inicializa o valor de h (o gap) usando a sequência de 
Knuth (h = h * 3 + 1). Isso cria uma série de gaps que são cada vez menores, até que o gap seja 1, o que 
torna o algoritmo equivalente ao Insertion Sort.
                Ordenação com Gaps: Com cada valor de h, o algoritmo percorre a lista em intervalos de h posições,
comparando elementos que estão h posições distantes e realizando trocas se necessário. Isso é semelhante ao 
Insertion Sort, mas aplicado a elementos distantes uns dos outros.
                Redução Gradual do Gap: Após ordenar os elementos com um determinado gap h, o algoritmo reduz 
o valor de h para h // 3 (de acordo com a sequência de Knuth) e repete o processo até que h seja 1, momento em que
o algoritmo faz um último passe de Insertion Sort, garantindo que a lista esteja totalmente ordenada.

complexidade de tempo: O(n^125)

"""

def main(x):
    w = 0  # Quantidade de vezes que entrou no laço mais interno (trocas)
    h = 1
    n = len(x)  # Tamanho da lista

    # Define o maior gap (h) possível baseado na sequência de Knuth
    while h < n:
        h = h * 3 + 1  # Gaps são 1, 4, 13, 40, etc.

    # Inicia o processo de ordenação diminuindo gradualmente o gap h
    while h > 1:
        h = h // 3  # Reduz o gap de acordo com a sequência de Knuth
        for i in range(h, n, h):  # Inicia o Insertion Sort com gap h
            atual = x[i]
            j = i - h

            # Compara e move elementos conforme necessário
            while j >= 0 and atual < x[j]:
                w = w + 1  # Incrementa a contagem de trocas
                x[j + h] = x[j]
                j = j - h
            x[j + h] = atual

    print(f'Quantidade de trocas foi {w} vezes no shell sort')
