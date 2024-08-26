def main(x):
    w = 0 # quantidade de vezes em que entrou no laço mais externo
    n = len(x)
    for i in range(1, n):
        v = x[i]
        j = i
        while j > 0 and x[j - 1] > v:
            w = w + 1  # incrementa a quantidade de trocas            
            x[j] = x[j - 1]
            j = j - 1
        x[j] = v
    print(f'Quantidade de trocas foi {w} vezes no insertion sort')
