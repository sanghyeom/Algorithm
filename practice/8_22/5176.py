T = int(input())
'''
              1  2  3  4  5  6  7   8  9  10  11  12  13
left_child  [ 2  4  6  8  10 12  -  -  -  -   13   -   -]
right_child [ 3  5  7  9  11 13  -  -  -  -   -    -   -]

'''

for tc in range(1,T+1):
    N = int(input())
    node_left = [0] * (N+1)
    node_right = [0] * (N+1)

    idx = 1
    cnt = 2
    while cnt < N+1 : 
        node_left[idx] = cnt
        cnt += 1
        if cnt >= N :
            break
        node_right[idx] = cnt
        idx += 1
        cnt += 1
   
    def f(root):
        # root : 현재 탐색하고 있는 트리의 루트 노드
        
        # 유도 조건
        # 자식이 있다면, 해당 자식을 중심으로 순회
        if node_left[root] != 0: # 왼쪽 자식이 있다면
            f(node_left[root])
        print(root, end=' ')
        if root == 3 :
            print('나온다구',root)
        if node_right[root] != 0: # 오른쪽 자식이 있다면
            f(node_right[root])

    print("트리 전위순회 시작")
    f(1) # 1번 노드를 중심으로 순회
    print()
    print("트리 전위순회 끝")
    
