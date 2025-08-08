T = int(input())
for Test_case in range(1,T+1):
    N , M= map(int,input().split())
    # 파리 리스트 업로드
    pan = []
    for _ in range(N):
        pan.append(list(map(int,input().split())))
    
    # 부분 
    max_fly = 0 
    for x in range(N-M+1):
        for y in range(N-M+1):
            fly_sum =0
            for k in range(M):
                for h in range(M):
                    fly_sum += pan[x+k][y+h]
            if fly_sum > max_fly:
                max_fly = fly_sum


    print(f'#{Test_case} {max_fly}')