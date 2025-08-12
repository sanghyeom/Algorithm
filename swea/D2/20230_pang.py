T = int(input())

for tc in range(1,T+1):
    N = int(input())
    pan = [0]*N
    for i in range(N):
        pan[i] = list(map(int,input().split()))

    print(pan)
