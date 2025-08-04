T = int(input())

for Test_case in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    max_ai = 0
    min_ai = ai[0]
    total = 0
    for i in range(N) :
        if ai[i] > max_ai :
            max_ai = ai[i]
        if ai[i] <= min_ai :
            min_ai = ai[i]
    total = max_ai - min_ai
    print(f'#{Test_case} {total}')