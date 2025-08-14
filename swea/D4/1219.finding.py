for _ in range(10):
    tc , M = list( map(int,input().split()))
    total_li = list(map(int,input().split()))
    node_li = [0] * M
    for i in range(M):
        node_li[i] = ( total_li[2*i],total_li[2*i +1] )

    adj = [[] for _ in range(100)]
    for i in node_li :
        adj[i[0]].append(i[1])

    #시작점 0  도착점 99
    stack = []
    connected = False
    visited = [0] * 100 # 방문처리 배열
    # 0으로 초기화(아직 아무 노드도 방문하지 않음.)
    # visited[1] == 0: 1을 방문하지 않은 상황
    # visited[1] == 1: 1을 이미 방문
    # visited[V] == 1: V 노드를 방문했음.


    # 1. 시작 점을 방문처리후 스택에 넣는다.
    visited[0] = 1

    stack.extend(adj[0])
    while stack: # stack이 비어있지 않다면
        # 2.1. stack에서 top을 제거
        v = stack.pop() # 현재 스택의 가장 위에 있는 노드 부터 방문
        if v == 99: 
            # print("도착점 방문!")
            connected = True
            break

        #adj[v]: v점에서 갈수있는 노드들(인접 노드)
        for w in adj[v]: # 인접 노드를 모두 검사
            if visited[w] == 0: # 아직 w를 방문하지 않았다면
                visited[w] = 1 # 방문 처리 후에
                stack.append(w) # 스택에 넣는다.

    if connected:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
