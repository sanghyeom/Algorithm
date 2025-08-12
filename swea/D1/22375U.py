T = int(input())

for tc in range(1,T+1):
    N= int(input())
    st_swich = list(map(int,input().split()))
    ed_swich = list(map(int,input().split()))

    cnt =0 
    for i in range(N) :
        if st_swich[i] != ed_swich[i]:
            cnt +=1
            for x in range(i,N):
                st_swich[x] ^=1
                st_swich[x] ^=0
                

    print(f'#{tc}',cnt)
