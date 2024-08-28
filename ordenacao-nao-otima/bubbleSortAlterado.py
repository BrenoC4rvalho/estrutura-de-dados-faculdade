def main(x):
    w = 0 # quantidade de vezes em que entrou no laço mais externo
    n = len(x)
    for j in range(0, n - 1):
        trocou = False
        for i in range(n - 1, j, -1):
            w = w + 1  # incrementa a quantidade de trocas
            
            if x[i - 1] > x[i]:
                trocou = True
                z = x[i]
                x[i] = x[i - 1]
                x[i - 1] = z
        if not trocou:
            break

    print(x)

import random

k = []
for i in range(random.randint()):
    k.append(i)

print(k)
main(k)
