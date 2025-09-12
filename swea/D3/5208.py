T = int(input())

for TC in range(1, T + 1):
    bus_map = list(map(int, input().split()))
    
    goal = bus_map[0] - 1
    bus_stop = bus_map[1:] + [-1]

    position = 0
    cnt = 0

    while position < goal:
        # 도착 가능하면 충전 없이 종료
        if position + bus_stop[position] >= goal:
            break  # ❗ 여기서 cnt += 1 하지 마세요

        max_reach = 0
        next_pos = -1

        for i in range(position + 1, min(position + 1 + bus_stop[position], len(bus_stop))):
            if i + bus_stop[i] > max_reach:
                max_reach = i + bus_stop[i]
                next_pos = i

        if next_pos == -1:
            break

        position = next_pos
        cnt += 1

    print(f'#{TC} {cnt}')
