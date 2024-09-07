""" 

definição: é um algoritmo de ordenação baseado no paradigma "dividir e conquistar". Ele divide a lista em 
partes menores, ordena cada parte recursivamente e, em seguida, combina as partes ordenadas para obter a lista
final ordenada.

comportamento:  Dividir: O algoritmo divide a lista em duas metades até que cada sublista contenha um único elemento ou 
esteja vazia (base da recursão).
                Conquistar: Ordena cada sublista (em termos práticos, isso acontece ao combinar as sublistas ordenadas).
                Combinar: Junta as sublistas ordenadas em uma lista ordenada.

complexidade de tempo: O(n log n)

"""


def mergeSort(x):
    # Inicia o processo de ordenação chamando a função merge com a lista e seus limites
    merge(x, 0, len(x))

def merge(x, ini, fim):
    # Ordena a sublista de x[ini:fim] se tiver mais de um elemento
    if fim - ini > 1:
        meio = (fim + ini) // 2  # Encontra o índice do meio
        # Ordena recursivamente as duas metades
        merge(x, ini, meio)
        merge(x, meio, fim)
        # Concatena as duas metades ordenadas
        concatena(x, ini, meio, fim)

def concatena(x, ini, meio, fim):
    # Cria sublistas para a fusão
    pi = x[ini:meio]  # Sublista da primeira metade
    pf = x[meio:fim]  # Sublista da segunda metade
    i, f = 0, 0  # Índices para as sublistas
    # Percorre a lista original para combinar as sublistas ordenadas
    for k in range(ini, fim):
        if i >= len(pi):  # Se todos os elementos da primeira sublista foram usados
            x[k] = pf[f]  # Copia o próximo elemento da segunda sublista
            f = f + 1
        elif f >= len(pf):  # Se todos os elementos da segunda sublista foram usados
            x[k] = pi[i]  # Copia o próximo elemento da primeira sublista
            i = i + 1
        elif pi[i] < pf[f]:  # Se o elemento da primeira sublista é menor
            x[k] = pi[i]  # Copia o elemento da primeira sublista
            i = i + 1
        else:  # Se o elemento da segunda sublista é menor ou igual
            x[k] = pf[f]  # Copia o elemento da segunda sublista
            f = f + 1

x = [1, 5, 9, 3, 4, 8, 11, 2, 0]

mergeSort(x)
print(x)
