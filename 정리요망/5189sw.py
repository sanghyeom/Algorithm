T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = [0] * N
    for i in range(N):
        rooms[i] = list(map(int, input().split()))

    visit = [False] * N
    result = 999999

    def pic_room(S, cnt, sum_E):
        global result
        if cnt == N:
            sum_E += rooms[S][0]
            result = min(result, sum_E)
            return

        for x in range(N):
            if not visit[x]:
                visit[x] = True
                pic_room(x, cnt + 1, sum_E + rooms[S][x])
                visit[x] = False

    visit[0] = True
    pic_room(0, 1, 0)
    print(f'#{tc}'result)
