from pprint import pprint 
T = int(input())

# 빈 N*N 2차원 리스트 생성
for Test_case in range(1,T+1):
    N =int(input())
    snail_num = []

    # 스타트 ##0
    for _ in range(N):
        snail_num.append([0]*N)
    
    #스타트 & 맨오른쪽 내려가기.
    for i in range(N):
        for j in range(N):
            snail_num[0][j] = j+1
            # if  i != 0 and j % N == N-1 :
            #     snail_num[i][j] = snail_num[i-1][j] +1
    

    # # 맨밑에서 뒤로올떄
    # for x in range(N-2,-1,-1):
    #     snail_num[N-1][x] = snail_num[N-1][x+1]+1

    # #올라올때
    # for y in range(N-2,0,-1):
    #     snail_num[y][0] = snail_num[y+1][0]+1

    # # 첫줄 패스 -> 다시 정렬
    # for q in range(1,N-1):
    #     snail_num[1][q] = snail_num[1][q-1]+1

    # # 다시 내려가기. 
    # for s in range(2,N-1) :
    #     snail_num[s][N-2] = snail_num[s-1][N-2] +1
    # # 중복시작 (뒤로가기)
    # for x in range(N-3,0,-1):
    #     snail_num[N-2][x] = snail_num[N-2][x+1]+1

    # #올라올때
    # for y in range(N-3,1,-1):
    #     snail_num[y][1] = snail_num[y+1][1]+1


    CP = N
    x = 1
    y = N-1

    while CP < ((1+(N*N))*(N*N)/2):
        while snail_num[N-1][N-1] == 0 :
            snail_num[x][y] = snail_num[x-1][y]+1
            x += 1
            CP += 1
            if snail_num[N-1][N-1] != 0 :
                break
        print('여가문제니?')
    print(f'#{Test_case}')
    pprint(snail_num)