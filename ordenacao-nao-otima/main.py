import random  # Importa o módulo para gerar números aleatórios
import bubbleSort, insertionSort, selectionSort, shellSort  # Importa os módulos dos algoritmos de ordenação

flag = True  # Inicializa a flag para controlar o loop

while flag:
    # Exibe o menu principal de opções
    print("""
        Algoritmos de ordenação
    """)

    # Exibe as opções para criar ou utilizar uma lista
    print("""
        Você deseja criar ou utilizar uma lista aleatória?
        1 - Criar
        2 - Lista aleatória     
        3 - Lista com 1000 posições Ordenada
        4 - Lista com 1000 posições Decrescente
    """)

    x = []  # Inicializa uma lista vazia
    # Solicita ao usuário a escolha do método para criar a lista
    choice_method_create_list = int(input("Escolha uma das opções:  "))
    
    # Cria a lista com base na escolha do usuário
    if choice_method_create_list == 1:
        number = int(input("Adicione um número: \n"))
        # Adiciona números na lista até que o usuário digite -1
        while number > -1:
            x.append(number)  # Adiciona o número à lista
            number = int(input("Caso não queira mais adicionar um número, digite -1, caso contrário adicione um número:"))
    elif choice_method_create_list == 2:
        quantity = int(input("Quantos números terá na lista:"))
        # Preenche a lista com números aleatórios
        for i in range(quantity):
            x.append(random.randint(0, quantity * 10))
    elif choice_method_create_list == 3:
        # Cria uma lista ordenada com 1000 elementos
        for i in range(1000):
            x.append(i)
    elif choice_method_create_list == 4:
        # Cria uma lista ordenada decrescentemente com 1000 elementos
        for i in range(999, -1, -1):
            x.append(i)

    # Exibe as opções de algoritmos de ordenação
    print("""
        Qual algoritmo de ordenação você quer testar? 
        1 - Bubble Sort
        2 - Selection Sort
        3 - Insertion Sort
        4 - Shell Sort
        5 - Todos
        6 - Exit    
    """)

    # Solicita ao usuário a escolha do algoritmo de ordenação
    choice_algorithm = int(input("Escolha uma das opções: "))

    # Exibe a lista que será ordenada
    print(f"""
        A lista que será ordenada é:
        {x}
    """)

    # Executa o algoritmo de ordenação escolhido
    match choice_algorithm:
        case 1:
            bubbleSort.main(x.copy())  # Ordena a lista usando o Bubble Sort
        case 2:
            selectionSort.main(x.copy())  # Ordena a lista usando o Selection Sort
        case 3:
            insertionSort.main(x.copy())  # Ordena a lista usando o Insertion Sort
        case 4:
            shellSort.main(x.copy())  # Ordena a lista usando o Shell Sort
        case 5:
            bubbleSort.main(x.copy())  # Ordena a lista usando todos os algoritmos
            selectionSort.main(x.copy())
            insertionSort.main(x.copy())
            shellSort.main(x.copy())
        case 6:
            flag = False  # Sai do loop
            break
        case _:
            print("Opção inválida. Tente novamente.")  # Mensagem para opções inválidas
