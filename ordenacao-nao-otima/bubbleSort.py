def main(x):
    w = 0 # quantidade de vezes em que entrou no laço mais externo
    n = len(x)
    for j in range(0, n - 1):
        for i in range(n - 1, j, -1):
            w = w + 1  # incrementa a quantidade de trocas
            
            if x[i - 1] > x[i]:
                z = x[i]
                x[i] = x[i - 1]
                x[i - 1] = z

    print(f'Quantidade de trocas foi {w} vezes no bubble sort')
