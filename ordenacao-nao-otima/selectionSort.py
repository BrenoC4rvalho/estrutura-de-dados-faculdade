def main(x):
    w = 0 # quantidade de vezes em que entrou no laço mais externo
    n = len(x)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            w = w + 1  # incrementa a quantidade de trocas
            if x[i] > x[j]:
                z = x[i]
                x[i] = x[j]
                x[j] = z
    print(f'Quantidade de trocas foi {w} vezes no selection sort')
