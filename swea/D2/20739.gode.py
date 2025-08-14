T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    picture = [0] * N
    for i in range(M):
        picture[i] = list(map(int,input().split()))
    x_max = 0
    y_max = 0
    x_lit = [0]*N 
    y_lit = [0]*M

    for i in range(N):    
        x_max = 0
        for j in range(M):
            x_max += picture[i][j]      
        x_lit[i] = x_max
    for i in range(M):    
        y_max = 0
        for j in range(N):
            y_max += picture[j][i]      
        y_lit[i]=y_max

    max_build = 0 
    for i in range(N):
        if max_build < x_lit[i]:
            max_build = x_lit[i]
    for j in range(M):
        if max_build < y_lit[j]:
            max_build = y_lit[j]
    
    if max_build < 2 : 
         max_build =0 
    print(f'#{tc} {max_build}')