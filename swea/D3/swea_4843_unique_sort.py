T = int(input())



for Test_case in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    max_num = 0
    min_num = 0 
    result =[]

    for z in range(5):
        for i in range(N-2*z) :
            if max_num < ai[i] :
                max_num = ai[i] 
        min_num = max_num    
        for i in range(N-2*z) :
            if min_num > ai[i] :
                min_num = ai[i]

        
        result.append(max_num)
        ai.remove(max_num)
        result.append(min_num)
        ai.remove(min_num)
        max_num = 0
    
    print(f"#{Test_case} {' '.join(map(str,result))}")