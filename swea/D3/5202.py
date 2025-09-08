T = int(input())
for TC in range(1,T+1):
    N = int(input())
    time_line = []     
    for i in range(N):
        s,e = map(int, input().split())
        time_line.append((e,s))
    time_line.sort()
    cnt = 0 
    end_time = 0
    result = 0 
    while cnt <len(time_line) : 
        if end_time <= time_line[cnt][1]:
            end_time=time_line[cnt][0]
            result+=1
        cnt +=1
    print(f'#{TC}',result) 

    

'''
3
5
20 23
17 20
23 24
4 14
8 18
'''