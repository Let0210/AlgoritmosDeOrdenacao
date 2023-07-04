import math

class HeapSort:
    def __init__(self, vetor):
        self.vetor = vetor

    def sort(self):
        self.heapsort(self.vetor)

    def constroiHeapMax(self, vetor, tamHeap):
        for i in range(math.floor(len(vetor) / 2) - 1, -1, -1):
            self.refazHeapMax(vetor, tamHeap, i)

    def refazHeapMax(self, vetor, tamHeap, i):
        filho_esq = 2 * i + 1
        filho_dir = 2 * i + 2
        maior = i

        if filho_esq < tamHeap and vetor[filho_esq] > vetor[maior]:
            maior = filho_esq

        if filho_dir < tamHeap and vetor[filho_dir] > vetor[maior]:
            maior = filho_dir

        if maior != i:
            aux = vetor[i]
            vetor[i] = vetor[maior]
            vetor[maior] = aux
            self.refazHeapMax(vetor, tamHeap, maior)

    def heapsort(self, vetor):
        tamHeap = len(vetor)
        self.constroiHeapMax(vetor, tamHeap)

        for i in range(len(vetor) - 1, 0, -1):
            aux = vetor[0]
            vetor[0] = vetor[i]
            vetor[i] = aux

            tamHeap = tamHeap - 1
            self.refazHeapMax(vetor, tamHeap, 0)
