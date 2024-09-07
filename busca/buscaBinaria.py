""" 

definição: é um algoritmo eficiente para encontrar um elemento específico em uma lista ordeanda de elementos.
O algoritmo funciona dividindo repetidamente a lista pela metade e comparando o elemento do meio com o valor 
do alvo. Dependendo do resultado da comparação, ele contínua a busca na metade superior ou inferior da lista
até encontrar o elemento ou reduzir o tamanho da lista para zero, indicando que o elemento não está presente.

comportamento:  Comece com dois ponteiros, um no início (esquerda) e outro no final (direita) da lista.
                Calcule o índice do meio como (esquerda + direita) // 2.
                Compare o elemento no meio com o valor alvo.
                    Se for igual, o elemento foi encontrado.
                    Se o valor no meio for maior que o alvo, ajuste o ponteiro da direita para meio - 1.
                    Se o valor no meio for menor que o alvo, ajuste o ponteiro da esquerda para meio + 1

complexidade de tempo: O(log n)

"""

def buscaBinaria(x, v):
    li = 0  # Índice inicial da lista (limite inferior)
    ls = len(x) - 1  # Índice final da lista (limite superior)

    # Enquanto o limite inferior não ultrapassar o limite superior
    while li <= ls:
        i = (li + ls) // 2  # Calcula o índice do meio da lista

        # Se o valor no meio é igual ao valor procurado, retorna o índice
        if v == x[i]:
            return i
        
        # Se o valor procurado é menor que o valor no meio,
        # ajusta o limite superior para buscar na metade inferior
        elif v < x[i]:
            ls = i - 1
        
        # Se o valor procurado é maior que o valor no meio,
        # ajusta o limite inferior para buscar na metade superior
        else:
            li = i + 1

    # Se o valor não foi encontrado, retorna -1
    return -1


x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(buscaBinaria(x, 13))