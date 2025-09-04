N = int(input())
path = []
visit = [False] * (N+1)
def base(cnt) :
    if cnt == N :
        print(*path)
        return
    for num in range(1,N+1):
        if visit[num] :
            continue
        visit[num] = 1
        path.append(num)
        base(cnt+1)
        visit[num] = 0
        path.pop()    
base(0)