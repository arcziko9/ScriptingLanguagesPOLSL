# Zadanie 110

def gauss(a, b):
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                b[j][k] -= t * b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        t = 1 / a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return b

def showMatrix(A):
    n = len(A)
    for i in range(n):
        line = "|"
        for j in range(n):
            line += str(A[i][j]).center(30)
            if j == n-1:
                line += "|"
        print(line)
    print("")


a = [[3, 3, 1], [5, 4, 8], [7, 3, 4]]
b = [[7, 6, 7], [2, 3, 1], [1, 1, 8]]
c = gauss(a, b)

showMatrix(c)