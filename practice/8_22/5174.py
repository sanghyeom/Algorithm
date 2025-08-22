T= int(input())
for tc in range(1,T+1):
    E , N = map(int,input().split())
    map_li = list(map(int,input().split()))

    node_L = [0] * len(map_li)
    node_R = [0] * len(map_li)

    for i in range(E):
        if node_L[map_li[2*i]] != 0:
            if node_L[ map_li[2*i] ] > map_li[(2*i)+1]:
                node_R[ map_li[2*i] ] = node_L[ map_li[2*i] ]
                node_L[ map_li[2*i] ] = map_li[(2*i)+1]
            else : 
                node_R[ map_li[2*i] ] = map_li[(2*i)+1]
        else : 
            node_L[ map_li[2*i] ] = map_li[(2*i)+1] 

    cnt = 1 
    def find(A):
        global cnt
        if node_L[A] != 0 :
            cnt+=1
            find(node_L[A])
        if node_R[A] != 0 :
            cnt+=1
            find(node_R[A])
        if node_L[A] == 0 and node_R[A] == 0:
            return cnt
    find(N)
    print(f'#{tc} {cnt}')
