T = int(input())
for TC in range(1,T+1) : 
    N = int(input())
    lines = [0]*10001
    cnt = 0 
    same_lines = []
    sort_lines = []

    for i in range(N):
        a, b = map(int,input().split())
        if a == b :
            same_lines.append((a,b))
        else : 
            sort_lines.append((b,a))
    sort_lines.sort()

    for i,j in same_lines :
        lines[i] +=1   

    for i,j in sort_lines :   
        if i > j :
            for x in range(j,i+1):
                if lines[x] != 0 :
                    cnt +=1 
        else : 
            for x in range(i,j+1):
                if lines[x] != 0 :
                    cnt +=1 

        
    print(f'#{TC}',cnt)

