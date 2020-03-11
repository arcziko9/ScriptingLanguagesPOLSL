# Zadanie 94
from cmath import e

def crout(A):
    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]

    for j in range(n):
        U[j][j] = 1

        for i in range(j, n):
            alpha = float(a[i][j])
            for k in range(j):
                alpha -= L[i][k] * U[k][j]

            L[i][j] = alpha

        for i in range(j+1, n):
            tempU = float(A[j][i])
            for k in range(j):
                tempU -= L[j][k] * U[k][i]

            if int(L[j][j]) == 0:
                L[j][j] = e-40

            U[j][i] = tempU/L[j][j]

    return [L, U]

a = [[6, 3, 1], [2, 8, 7], [1, 0, 0]]
print(crout(a))