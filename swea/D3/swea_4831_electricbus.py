T = int(input())

for Test_case in range(1,T+1):
    K,N,M = map(int,input().split()) # 최대 이동수 # 도착 정류장 # 충전기 개수
    
    Charge_list = list(map(int,input().split())) # 충전기 위치
    Charge_list_convert = [0] * (N+1)
    for j in range(M) :
        Charge_list_convert[Charge_list[j]] += 1
    
    min_charge = 0 
    bus = 0
    while bus + K <N :
        for findcharge in range(K-1,-1,-1):
            position = bus + findcharge + 1
            if Charge_list_convert[position] == 1 :                
                min_charge +=1 
                bus += findcharge+1
                break
        else :
            min_charge = 0
            break



    print(F'#{Test_case} {min_charge}')
