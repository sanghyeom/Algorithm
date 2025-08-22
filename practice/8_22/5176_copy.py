T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0]* (N+1)
    cnt = 1
    
    def make(a) : 
        global cnt
        if a > N :
            return
        make(2*a)
        tree[a] = cnt
        cnt += 1
        make((2*a)+1)
    make(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')