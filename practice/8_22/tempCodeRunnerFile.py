     # root : 현재 탐색하고 있는 트리의 루트 노드
        print(root, end=' ')
        # 유도 조건
        # 자식이 있다면, 해당 자식을 중심으로 순회
        if node_left[root] != 0: # 왼쪽 자식이 있다면
            f(node_left[root])
        if node_right[root] != 0: # 오른쪽 자식이 있다면
            f(node_right[root]) 









                idx = 1
    cnt = 2
    while cnt < N : 
        node_left[idx] = cnt
        cnt += 1
        node_right[idx] = cnt
        idx += 1
        cnt += 1