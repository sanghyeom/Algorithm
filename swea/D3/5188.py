T = int(input())

for TC in range(1,T+1):
    N = int(input())

    PAN = [0] * N
    for i in range(N):
        PAN[i] = list(map(int,input().split()))
