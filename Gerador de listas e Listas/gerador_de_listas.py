# Codigo para criar listas csv com 500.000 numeros aleatorios
# Melhor NÃO rodar!

import csv
import random

quantidade = 500000 

for i in range(1, 5):
    numeros = random.sample(range(1, 10000000), quantidade)

    with open(f"lista{i}.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(numeros)

    print(f"lista{i}.csv criada")