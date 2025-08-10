T = int(input())

for testcase in range(1,T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # 초기위치 설정
    r , c = 0 , 0
    #회전방향 설정
    dist = 0 # 0 우 1 하 2 좌 3 상
    dx, dy = [1,0,-1,0],[0,1,0,-1]


    for i in range(1, N*N + 1):
        snail[r][c] = i
        r += dy[dist]
        c += dx[dist]
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0 :
            r -= dy[dist]
            c -= dx[dist]
            dist = (dist+1) % 4
            r += dy[dist]
            c += dx[dist]

    print(f'#{testcase}')
    for row in snail :
        print(*row)