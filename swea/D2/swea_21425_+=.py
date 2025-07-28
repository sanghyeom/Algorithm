T = int(input())

for Test_case in range(1,T+1):
    N = list(map(int,input().split()))
    count = 0
    if N[0] >=N[1]:
        MAX = N[0]
        MIN = N[1]
    else :
        MAX = N[1]
        MIN = N[0]

    while MAX <= N[2] :
        # print(N[2],MIN,MAX)
        A = 0
        MIN = MAX + MIN
        if MAX <= MIN :
            A = MAX
            MAX = MIN
            MIN = A
        count +=1
        if MAX > N[2] :
            break
    print(f'{count}')