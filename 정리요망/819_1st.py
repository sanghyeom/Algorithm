N = 5
P = [0,1,1,2,0]

visited_max_idx = 0 
idx  = 1
cnt = 1 

visited[idx] = True

while idx < N :

    idx +=1
    cnt+=1
    print(idx , cnt)

    if idx == N :
        break

    if not visited[idx]:
        visited[idx] = True
        idx = P[idx] # 왼쪽으로 이동 
        cnt += 1 # 이동했으니 카운트 
