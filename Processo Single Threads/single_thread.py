# Esse codigo organiza 4 listas com 500.000 numeros aleatorios e cria novas listas em arquivos csv com uma unica thread
import csv
import time
import os


for i in range(1, 5): # Esse for serve pra excluir as listas organizadas se elas existirem para poder refazer o processo

    nome_arquivo = f"Gerador de listas e Listas/lista{i}_ordenado_single.csv"

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
            numeros = [int(n) for n in linha]

    numeros.sort()

    with open(nome_arquivo.replace(".csv", "_ordenado_single.csv"), "w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(numeros)

    print(f"{nome_arquivo} ordenado")


for i in range(1, 5):

    ordenar_arquivo(f"Gerador de listas e Listas/lista{i}.csv")


fim = time.time() # fim do cronometro

print(f"\nTempo total de execução: {fim - inicio:.2f} segundos")
print("Para visualizar as listas vá na pasta 'Gerador de listas e Listas'")