
N, K = 5, 3
arr = [[0, 0, 1, 1, 1], 
       [1, 1, 1, 1, 0], 
       [0, 0, 1, 0, 0], 
       [0, 1, 1, 1, 1], 
       [1, 1, 1, 0, 1]]

result = 0

# 행 순회
for r in range(N):
    cnt = 0
    for c in range(N):
        a = arr[r][c] 
        '''
        0 0 1 1 1 
        1 1 1 1 0
        0 0 1 0 0
        0 1 1 1 1
        1 1 1 0 1
        '''
        if a == 1:
            cnt += 1
        if a==0 or c == N-1 :
            if cnt == K:
                print(arr[r][c],r, c, cnt)
                result += 1
                cnt = 0
print(result)