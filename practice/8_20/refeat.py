T = int(input())

for tc in range(1,T+1):
    N, M  = map(int,input().split())
    num_list = list(map(int,input().split()))
    num = ( M % N )
    print(f'#{tc}',num_list[num])