def main(x):
    w = 0 # quantidade de vezes em que entrou no laço mais externo
    h = 1
    n = len(x)
    while h < n:
        h = h * 3 + 1
    while h > 1:
        h = h // 3
        for i in range(h, n, h):
            atual = x[i]
            j = i - h
            while j >= 0 and atual < x[j]:
                w = w + 1  # incrementa a quantidade de trocas
                x[j + h] = x[j]
                j = j - h
            x[j + h] = atual
    print(f'Quantidade de trocas foi {w} vezes no shell sort')
