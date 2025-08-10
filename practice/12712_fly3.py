T = int(input())

for testcase in range(1,T+1):
    N, M = map(int, input().split())
    flypan = []
    for _ in range(N):
        flypan.append(list(map(int, input().split())))
    
    # + 범위 구현
    dx,dy = [1,-1,0,0],[0,0,1,-1]

    #x  범위 구현
    ddx , ddy = [1,1,-1,-1],[1,-1,-1,1]

    best_sum = 0
    check_sum_P = 0
    check_sum_C = 0
    for i in range(N):
        for j in range(N):
            check_sum_P = flypan[i][j]
            check_sum_C = flypan[i][j]
            for x in range(4):
                for r in range(1,M):             
                    if 0 <= i+dx[x]*r < N and 0 <= j+dy[x]*r <N :
                        check_sum_P += flypan[i+dx[x]*r][j+dy[x]*r]
                    if 0 <= i+ddx[x]*r < N and 0 <= j+ddy[x]*r <N :
                        check_sum_C += flypan[i+ddx[x]*r][j+ddy[x]*r]
            if check_sum_P > best_sum :
                best_sum = check_sum_P
            if check_sum_C > best_sum :
                best_sum = check_sum_C



    print(f'#{testcase} {best_sum}')