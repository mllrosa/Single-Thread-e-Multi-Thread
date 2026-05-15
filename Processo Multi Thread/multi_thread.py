# Esse codigo organiza 4 listas com 500.000 numeros aleatorios e cria novas listas em arquivos csv com uma 4 thread's

import csv
import time
from threading import Thread
import os


for i in range(1, 5): # Esse for serve pra excluir as listas organizadas se elas existirem para poder refazer o processo

    nome_arquivo = f"Gerador de listas e Listas/lista{i}_ordenado_multi.csv"

    if os.path.exists(nome_arquivo):

        os.remove(nome_arquivo)

        print(f"{nome_arquivo} removido")

    else:
        print(f"{nome_arquivo} NÃO existe")



inicio = time.time() # O tempo só é contado a partir daqui porque é apatir daqui que inicia o processo

def ordenar_arquivo(nome_arquivo):

    with open(nome_arquivo, newline="", encoding="utf-8") as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            numeros = [int(numero) for numero in linha]

    numeros.sort()

    print(f"{nome_arquivo} ordenado")

    with open(
        f"{nome_arquivo.replace('.csv', '')}_ordenado_multi.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(numeros)


threads = []


for i in range(1, 5):

    t = Thread(
        target=ordenar_arquivo,
        args=(f"Gerador de listas e Listas/lista{i}.csv",)
    )

    threads.append(t)

    t.start()


for t in threads:
    t.join()

fim = time.time() # fim do cronometro


print(f"\nTempo total de execução: {fim - inicio:.2f} segundos")
print("Todas as threads finalizaram")
print("Para visualizar as listas vá na pasta 'Gerador de listas e Listas'")