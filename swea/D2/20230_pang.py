T = int(input())

for tc in range(1,T+1):
    N = int(input())
    pan = [0]*N
    for i in range(N):
        pan[i] = list(map(int,input().split()))

    row = [0]*N
    col = [0]*N
    sum_max = 0
    for i in range(N) :
        for j in range(N):
            row[i] += pan[i][j]
            col[i] += pan[j][i]
    for i in range(N) :
        for j in range(N):
            s= row[i]+col[j]-pan[i][j]
            if sum_max < s :
                sum_max= s
    print(f'#{tc}', sum_max)



# ---------------------------------------
# 디렉션두고 합 ; 