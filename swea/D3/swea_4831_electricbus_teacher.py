T = int(input())

def count_charge(K,N,M, Chargers ) :
    idx = 0 
    cot = 0

    while idx < N : 
        checkpo = [c for c in Chargers if idx < c and c <= idx+ K ]

    if idx + K >= N:
        return cot
    if len(checkpo) == 0 :
        return 0 



for Test_case in range(1,T+1):
    K,N,M = map(int,input().split()) # 최대 이동수 # 도착 정류장 # 충전기 개수
    Chargers = list(map(int,input().split())) # 충전기 위치
    
    min_charge=count_charge(K,N,M,Chargers)

    print(F'#{Test_case} {min_charge}')
