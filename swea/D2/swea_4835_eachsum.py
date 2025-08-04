T = int(input())

for Test_case in range(1,T+1):
    N , M= map(int,input().split())
    ai = list(map(int,input().split()))
    total = 0
    max_ai = 0
    min_ai = sum(ai)
    for i in range(N-M+1):

        check_each = 0
        for j in range(i,M+i):
            check_each += ai[j]
        if check_each > max_ai :
            max_ai = check_each
        if check_each <= min_ai :
            min_ai = check_each

    total = max_ai - min_ai


    print(f'#{Test_case} {total}')