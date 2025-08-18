T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = list(map(int,input().split()))

    P = int(input())
    B = [0] * P
    for i in range(P):
        B[i] = int(input())

    count_li =[0]  * P
    
    for i in range(N):
        for j in range(P):
            if A[i][0]<= B[j] <= A[i][1] : 
                count_li[j] +=1

        
    print(f'#{tc}', *count_li)