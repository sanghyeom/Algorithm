T = int(input())

for Test_case in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    max_ai = 0
    min_ai = ai[0]
    total = max(ai) - min(ai)
    print(f'#{Test_case} {total}')