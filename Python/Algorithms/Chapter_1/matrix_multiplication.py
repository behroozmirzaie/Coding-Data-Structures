a = [[2, 3], [4, 1]]
b = [[5, 7], [6, 8]]
c = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]

for i in range(len(c)):
    for j in range(len(c)):
        print(c[i][j], end=" ")
    print("")
