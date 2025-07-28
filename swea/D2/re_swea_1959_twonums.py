T = int(input())

for Test_case in range(1,T+1):
    N=list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    longer = B
    shorter = A
    totallst= []
    if len(A) >= len(B) : 
        longer = A
        shorter = B
    for j in range(len(shorter),len(longer)+1):
        ran = j - len(shorter) 
        total = 0 
        for i in shorter :
            total += i * longer[shorter.index(i)+ran]
        totallst.append(total)
    

    print(f'#{Test_case} {max(totallst)}')