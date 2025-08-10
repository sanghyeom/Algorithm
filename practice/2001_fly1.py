T = int(input())

for testcase in range(1,T+1):
    N, M = map(int, input().split())
    flypan = []
    for _ in range(N):
        flypan.append(list(map(int, input().split())))
    
    best_sum = 0
    check_sum = 0
    for i in range(N):
        for j in range(N):
            check_sum = 0   
            for x in range(M):
                for y in range(M): 
                    if i+x <N and j+y <N :
                        check_sum += flypan[i+x][j+y]
            if check_sum > best_sum :
                best_sum = check_sum



    print(f'#{testcase} {best_sum}')