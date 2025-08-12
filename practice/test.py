'''
홍보를위해 4행 n열 LED 설치 
1 on , 0 off 2가지상태 

(i,j) (i+j+1)이 시간 k 의 배수라면 현상태에서 다른 상태로바뀜.
ex 
k=2 0 k=3  1 

so 
'''

# N : 가로 크기 K : 시간  1상태의 갯수 구하기 

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    pan = [0]*4
    for i in range(4):
        pan[i] = [0]*N

    for i in range(4):
        for j in range(N):
            for time in range(1,K+1): 
                if (i+j+1) % time == 0 : 
                    if pan[i][j] == 1 :
                        pan[i][j] = 0 
                    elif pan[i][j] == 0 :
                        pan[i][j] = 1 
    sum_on=0
    for x in range(4):
        sum_on+=sum(pan[x])
        
    print(f'#{tc} {sum_on}')

        
 