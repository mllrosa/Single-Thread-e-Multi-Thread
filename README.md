# Sistemas Operacionais Tema: Uso de Single Thread e Multi Thread
Compreender o funcionamento de processos e em sistemas operacionais, analisando as diferenças entre aplicações que utilizam uma única () e aplicações com múltiplas ().

Foram desenvolvidos dois programas em python que realizam o processamento de uma grande quantidade de dados (ordenação de quatro arquivos csv).

### Objetivo
Comparar o desempenho entre aplicações Single Thread e Multi Thread utilizando Python.
O programa realiza a leitura de arquivos CSV contendo 500.000 números aleatórios, organiza os números em ordem crescente e salva novas listas organizadas.

| Método        | Média  |
| ------------- | ------ |
| Single Thread | 2.00 s |
| Multi Thread  | 2.41 s |

Apesar do uso de múltiplas threads permitir execução concorrente, o desempenho foi inferior ao Single Thread. Isso ocorre porque o Python possui um mecanismo chamado GIL (Global Interpreter Lock), que limita a execução paralela de threads em tarefas intensivas de processamento.