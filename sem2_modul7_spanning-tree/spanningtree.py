batasan = 9999999
N = 5
grafik = [[0, 19, 5, 0, 0],
         [19, 0, 5, 9, 2],
         [5, 5, 0, 1, 6],
         [0, 9, 1, 0, 1],
         [0, 2, 6, 1, 0]]

simpul = [0, 0, 0, 0, 0]
no_edge = 0
simpul[0] = True

print("Edge : Berat\n")

while (no_edge < N - 1):
    minimum = batasan
    a = 0
    b = 0
    for m in range(N):
        if simpul[m]:
            for n in range(N):
                if ((not simpul[n]) and grafik[m][n]):  
                    if minimum > grafik[m][n]:
                        minimum = grafik[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(grafik[a][b]))
    simpul[b] = True
    no_edge += 1
