T = int(input())

for TC in range(1,T+1):
    N,M = map(int, input().split())
    wi = list(map(int,input().split()))
    ti = list(map(int,input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)

    cnt = 0
    sum_weight = 0 
    for i in ti :
        while wi : 
            if cnt == len(wi):
                cnt = 0 
                break
            elif i < wi[cnt] :
                cnt += 1
                continue
            elif i >= wi[cnt] :
                sum_weight += wi.pop(cnt)
                cnt = 0 
                break

            

    print(f'#{TC}',sum_weight)
    
