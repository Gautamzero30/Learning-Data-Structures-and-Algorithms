import math
G = [
    [0,10,math.inf,5,math.inf],
    [math.inf, 0,1,2,math.inf],
    [math.inf,math.inf,0, math.inf,4],
    [math.inf ,3,9,0,2],
    [7, math.inf,6,math.inf,0]

]

def FW(W):
    n = len(W)
    D = dict()
    D[0] = W
    for K in range(n):
        D[K+1]= D[K]
        for i in range(n):
            for j in range(n):
                D[K+1][i][j] = min( D[K][i][j],D[K][i][K]+D[K][K][j]

                )
    print(D[K+1])
            
FW(G)

    
    

