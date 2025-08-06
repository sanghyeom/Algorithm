T = int(input())

for Test_case in range(1,T+1):
    N , M= map(int,input().split())
    pan = [0]* (N + (2*(M-1)))
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    ddx, ddy = [-1,1,1,-1], [1,1,-1,-1]
    for i in range(N):
        pan[i+(M-1)] = [0]*(M-1)+list(map(int,input().split()))+[0]*(M-1)
    maxi = 0 
    for x in range(M-1,N+M-1):
        for y in range(M-1,N+M-1):
            sum_xy = 0
            sum_notxy = 0
            for num in range(M):
                sum_notxy += pan[x+ddx[num]][y+ddy[num]]  
                sum_xy += pan[x+dx[num]][y+dy[num]]
                if sum_xy+pan[x][y] > maxi :
                    maxi = sum_xy+pan[x][y]

                sum_notxy += pan[x+ddx[num]][y+ddy[num]]  
                if sum_notxy+pan[x][y] > maxi :
                    maxi = sum_notxy+pan[x][y]



    print (pan)
    print(f'#{Test_case} ')