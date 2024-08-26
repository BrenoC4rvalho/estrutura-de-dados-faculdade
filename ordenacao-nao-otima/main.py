import random 
import bubbleSort, insertionSort, selectionSort, shellSort

flag = True

while flag :

    print("""
        Algoritimos de odernação
    """)

    print("""
        Você deseja criar ou utilizar uma lista aleátoria?
        1 - Criar
        2 - Lista aleátoria     
        3 - Lista com 1000 posições Ordernada
        4 - Lista com 1000 posições decrescente
    """)

    x = []
    choice_method_create_list = int(input("Escolha uma das opções:  "))
    
    if choice_method_create_list == 1:
        number = int(input("Adicione um número: \n"))
        while number > -1:
            x.append(number)
            number = int(input("Caso não queira mais adionar um número digite -1, caso contrário adicione um número:"))
    elif choice_method_create_list == 2:
        quantity = int(input("Quantos numeros terá na lista:"))
        for i in range(0, quantity):
            x.append(random.randint(0, quantity * 10))
    elif choice_method_create_list == 3:
        for i in range(0, 1000):
            x.append(i)
    elif choice_method_create_list == 4:
        for i in range(999, -1, -1):
            x.append(i)

    print("""
        Qual algoritmo de odernação você quer testar? 
        1 - Bubble Sort
        2 - Selection Sort
        3 - Insertion Sort
        4 - Shell Sort
        5 - Todos
        6 - Exit    
    """)

    choice_algorithm = int(input("Escolha uma das opções: "))

    print(f"""
        A lista que será ordernada é:
        {x}
    """)

    match choice_algorithm:
        case 1:
            bubbleSort.main(x.copy())
        case 2:
            selectionSort.main(x.copy())
        case 3:
            insertionSort.main(x.copy())
        case 4: 
            shellSort.main(x.copy())
        case 5:
            bubbleSort.main(x.copy())
            selectionSort.main(x.copy())
            insertionSort.main(x.copy())
            shellSort.main(x.copy())
        case 6:
            flag = False
            break
        case _:
            print("Opção inválida. Tente novamente.")    