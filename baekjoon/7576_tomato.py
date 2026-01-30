from collections import deque

m, n = map(int, input().split())
pan = [ list(map(int, input().split())) for _ in range(n) ]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs():
    q = deque([])

    for i in range(n):
        for j in range(m):
            if pan[i][j] == 1:
                q.append((i, j))

    while q:
        px, py = q.popleft()

        for k in range(4):
            mx = px + dx[k]
            my = py + dy[k]

            if 0 <= mx < n and 0 <= my < m:
                if pan[mx][my] == 0:
                    pan[mx][my] = pan[px][py] + 1
                    q.append((mx, my))

bfs()

answer = 0
for i in pan:
    answer = max(answer, max(i))

    if i.count(0):
        answer = 0
        break

print(answer-1)