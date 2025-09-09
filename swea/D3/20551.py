T = int(input())
for TC in range(1,T+1) : 
    A,B,C = map(int,input().split())

    result = -1
    cnt = 0
    
    while True :
        if C <= B : 
            B -= 1
            cnt +=1

            if C == 0 or B == 0 or A == 0 :
                break 

        elif B <= A :
            A -= 1
            cnt += 1
            if C == 0 or B == 0 or A == 0 :
                break 
        else : 
            result = max(cnt,result)
            break
    
    print(f'#{TC}',result)