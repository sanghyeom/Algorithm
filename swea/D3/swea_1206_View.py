for Test_case in range(1,11):
    N = int(input())
    ai = list(map(int,input().split()))
    total = 0
    for i in range(2,N-2):
        around_i = ai[i-2],ai[i-1],ai[i+2],ai[i+1]
        if ai[i]>max(around_i) :
            total += ai[i] - max(around_i)
    
    print(f'#{Test_case} {total}')