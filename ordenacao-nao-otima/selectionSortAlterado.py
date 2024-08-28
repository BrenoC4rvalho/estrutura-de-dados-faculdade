def main(x):
    w = 0 # quantidade de vezes em que entrou no laço mais externo
    n = len(x)
    for i in range(0, n - 1):
        trocou = False
        for j in range(i + 1, n):
            w = w + 1  # incrementa a quantidade de trocas
            if x[i] > x[j]:
                trocou = True
                z = x[i]
                x[i] = x[j]
                x[j] = z
        if not trocou:
            break 

    print(f'Quantidade de trocas foi {w} vezes no selection sort')

import random

k = []
for i in range(0, 15):
    k.append(random.randint(0, 100))

main(k.copy())