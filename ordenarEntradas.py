nome_arquivo = 'ordem aleatória/DuzentosMilNumsAleatorios.txt'

with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

numeros = [int(linha.strip()) for linha in linhas]

numeros_ordenados = sorted(numeros, reverse = True)

print(numeros_ordenados)

nome_arquivo = 'ordem decrescente/DuzentosMilDecrescente.txt'

with open(nome_arquivo, 'w') as arquivo:
    for numero in numeros_ordenados:
        arquivo.write(str(numero) + '\n')

print(f"Vetor gravado no arquivo {nome_arquivo} com sucesso!")
