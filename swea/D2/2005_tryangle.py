T = int(input())

for tc in range(1,T+1):
    N = int(input())
    result = []
    for i in range(1,N+1):
        result.append([1] * i)
        if i >=3 : 
            for j in range(2,i):
                
                result[i-1][j-1] = result[i-2][j-2]+result[i-2][j-1]    
    print(f'#{tc}',)
    for i in range(N):
        for j in range(len(result[i])):
            print(result[i][j],end = ' ')
        print()