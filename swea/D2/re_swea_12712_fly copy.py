T = int(input())

for Test_case in range(1,T+1):
    N , M= map(int,input().split())
    padding = (M-1)
    pan = [0]* (N + 2*padding )
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    ddx, ddy = [-1,1,1,-1], [1,1,-1,-1]
    for i in range(N):
        pan[i+padding] = [0]*padding+list(map(int,input().split()))+[0]*padding
    for z in range(padding):
        pan[z] = [0]* (N + 2*padding )
        pan[2*padding+N-1-z] = [0]* (N + 2*padding )

    result = 0 
    for x in range(N):
        for y in range(N):
            sum_dxy = pan[padding+x][padding+y]
            sum_ddxy = pan[padding+x][padding+y]

            for dir in range(1,M):
                for c in range(4):
                    sum_ddxy += pan[padding+x+ddx[c]*dir][padding+y+ddy[c]*dir]  
                    sum_dxy += pan[padding+x+dx[c]*dir][padding+y+dy[c]*dir]
                    if sum_dxy > result :
                        result = sum_dxy
    
                    if sum_ddxy > result :
                        result = sum_ddxy

    print(f'#{Test_case} {result}')