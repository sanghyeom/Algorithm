N, M = map(int, input().split())

for i in range(1,N+1):
    if m == 1 : 
        for for j in range(1,M+1):
            print(i)
    else:
        for j in range(1,N+1):
            if i == j : 
                continue
            else:
                print(i ,end=' ')
                print(j)