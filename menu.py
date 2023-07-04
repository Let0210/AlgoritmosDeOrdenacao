from mergesort import MergeSort
from heapsort import HeapSort
import time

nomeArquivo=""

def menuAlg():
    print("1. BubbleSort")
    print("2. InsertionSort")
    print("3. MergeSort")
    print("4. HeapSort")
    print("5. QuickSort")

def menuQtd():
    print("1. Cem")
    print("2. Mil")
    print("3. Cinco mil")
    print("4. Trinta mil")
    print("5. Cem mil")
    print("6. Cento e cinquenta mil")
    print("7. Duzentos mil")
    print("8. Sair")

def menuOrdemDeEntrada():
    print("1. Números já ordenados")
    print("2. Números em ordem decrescente")
    print("3. Números em ordem aleatória")


while True:
    print ("====MENU=====")
    print("")

    menuQtd()
    opcaoQtd = input ("Escolha a quantidade de números a serem ordenados: ")

    print("")
    menuOrdemDeEntrada()
    opcaoOrdemEnt = input ("Escolha a ordem do vetor de entrada a ser ordenado: ")

    if opcaoOrdemEnt =="1":
        if opcaoQtd =="1":
            nomeArquivo = "ordem Crescente/CemCrescente.txt"
        elif opcaoQtd =="2":
            nomeArquivo = "ordem Crescente/MilCrescente.txt"
        elif opcaoQtd =="3":
            nomeArquivo = "ordem Crescente/CincoMilCrescente.txt"
        elif opcaoQtd =="4":
            nomeArquivo = "ordem Crescente/TrintaMilCrescente.txt"
        elif opcaoQtd =="5":
            nomeArquivo = "ordem Crescente/CinquentaMilCrescente.txt"
        elif opcaoQtd =="6":
            nomeArquivo = "ordem Crescente/CentoECinquentaMilCrescente.txt"
        elif opcaoQtd =="7":
            nomeArquivo = "ordem Crescente/DuzentosMilCrescente.txt"

    if opcaoOrdemEnt =="2":
        if opcaoQtd =="1":
            nomeArquivo = "ordem decrescente/CemDecrescente.txt"
        elif opcaoQtd =="2":
            nomeArquivo = "ordem decrescente/MilDecrescente.txt"
        elif opcaoQtd =="3":
            nomeArquivo = "ordem decrescente/CincoMilDecrescente.txt"
        elif opcaoQtd =="4":
            nomeArquivo = "ordem decrescente/TrintaMilDecrescente.txt"
        elif opcaoQtd =="5":
            nomeArquivo = "ordem decrescente/CinquentaMilDecrescente.txt"
        elif opcaoQtd =="6":
            nomeArquivo = "ordem decrescente/CentoECinquentaMilDecrescente.txt"
        elif opcaoQtd =="7":
            nomeArquivo = "ordem decrescente/DuzentosMilDecrescente.txt"

    if opcaoOrdemEnt =="3":
        if opcaoQtd =="1":
            nomeArquivo = "ordem aleatória/CemAleatorios.txt"
        elif opcaoQtd =="2":
            nomeArquivo = "ordem aleatória/MilAleatorios.txt"
        elif opcaoQtd =="3":
            nomeArquivo = "ordem aleatória/CincoMilAleatorios.txt"
        elif opcaoQtd =="4":
            nomeArquivo = "ordem aleatória/TrintaMilAleatorios.txt"
        elif opcaoQtd =="5":
            nomeArquivo = "ordem aleatória/CinquentaMilAleatorios.txt"
        elif opcaoQtd =="6":
            nomeArquivo = "ordem aleatória/CentoECinquentaMilAleatorios.txt"
        elif opcaoQtd =="7":
            nomeArquivo = "ordem aleatória/DuzentosMilAleatorios.txt" 
                       
    with open(nomeArquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    vetorNum = [int(linha.strip()) for linha in linhas] 

    print("")
    menuAlg()
    opcaoAlg = input("Escolha um algoritmo de ordenação: ")
    
    if opcaoAlg == "1":
        print("Opção 1 selecionada.")
        # Faça algo relacionado à Opção 1

    elif opcaoAlg == "2":
        print("Opção 2 selecionada.")
        # Faça algo relacionado à Opção 2

    elif opcaoAlg == "3":
        mg = MergeSort(vetorNum)

        inicio = time.time()
        mg.sort()
        fim = time.time()
        tempo_decorrido = (fim-inicio) * 1000

    elif opcaoAlg == "4":
        hp = HeapSort(vetorNum)

        inicio = time.time()
        hp.sort()
        fim = time.time()
        tempo_decorrido = (fim-inicio) * 1000


    elif opcaoAlg == "5":
        print("Opção 2 selecionada.")
        # Faça algo relacionado à Opção 2

    else:
        print("Opção inválida. Tente novamente.")

    print(vetorNum)    
    print("")
    print(f"Tempo decorrido para ordenação: {tempo_decorrido:.2f} milissegundos")
    print("")