T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr =list(map(int,input()))
    # txt = input()
    max_v = 0 
    c = 0

    for i in range(N):
        if arr[i] ==1 :
            c += 1 
            if max_v < c :
                max_v = c 
        else :
            c = 0 

    print(F'#{tc} {max_v}')