import math

class MergeSort:
    def __init__(self, vetor):
        self.vetor = vetor

    def sort(self):
        self.mergesort(0, len(self.vetor) - 1)

    def mergesort(self, p, u):
        if p < u:
            q = math.floor((p + u) / 2)
            self.mergesort(p, q)
            self.mergesort(q + 1, u)
            self.merge(p, q, u)

    def merge(self, p, q, u):
        n1 = q - p + 1
        n2 = u - q
        L = []
        R = []

        for i in range(0, n1):
            L.append(self.vetor[p + i])

        for j in range(0, n2):
            R.append(self.vetor[q + j + 1])

        i = 0
        j = 0

        for k in range(p, u + 1):
            if i < n1 and (j >= n2 or L[i] <= R[j]):
                self.vetor[k] = L[i]
                i = i + 1
            else:
                self.vetor[k] = R[j]
                j = j + 1
