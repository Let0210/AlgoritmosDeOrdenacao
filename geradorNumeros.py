import random

def gerar_numeros_aleatorios(n):
    vetor = []
    for _ in range(n):
        numero_aleatorio = random.randint(1, 200000)  # Altere os limites conforme necessário
        vetor.append(numero_aleatorio)
    return vetor

tamanho_vetor = 200000
numeros_aleatorios = gerar_numeros_aleatorios(tamanho_vetor)

print(numeros_aleatorios)

nome_arquivo = 'DuzentosMilNumsAleatorios.txt'

with open(nome_arquivo, 'w') as arquivo:
    for numero in numeros_aleatorios:
        arquivo.write(str(numero) + '\n')

print(f"Vetor gravado no arquivo {nome_arquivo} com sucesso!")
