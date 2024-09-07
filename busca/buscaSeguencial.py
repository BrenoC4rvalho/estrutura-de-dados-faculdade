""" 

definição:  é um algoritmo simples para encontrar um valor em uma lista. O algoritmo percorre a lista 
do início ao fim, comparando cada elemento com o valor procurado até encontrá-lo ou até o final da 
lista ser alcançado. Também conhecida como busca linear

comportamento:  A Busca Sequencial é adequada para listas pequenas ou quando a lista não está ordenada. 
É simples e fácil de implementar, mas não é eficiente para listas grandes em comparação com algoritmos de 
busca mais avançados como a Busca Binária, que requer que a lista esteja ordenada.

complexidade de tempo: O(n)

"""

def busca_sequencial(lista, valor):
    """
    Função para realizar a busca sequencial (linear) em uma lista.

    :param lista: Lista de elementos onde o valor será procurado.
    :param valor: O valor que está sendo procurado na lista.
    :return: O índice do valor na lista se encontrado, caso contrário retorna -1.
    """
    # Percorre cada elemento da lista
    for i in range(len(lista)):
        # Compara o elemento atual com o valor procurado
        if lista[i] == valor:
            return i  # Retorna o índice se o valor for encontrado
    
    # Retorna -1 se o valor não for encontrado em toda a lista
    return -1
