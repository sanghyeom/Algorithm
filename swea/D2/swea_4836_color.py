T = int(input())

for Test_case in range(1,T+1):
    N = int(input())
    sq = []
    sq_red = []
    sq_blue = []
    result = 0
    # 리스트 입력
    for i in range(N):
        sq.append(list(map(int,input().split())))
    
    # 받은 인덱스 색별로 나누기
    for j in sq :
        if j[4] == 1 :
            sq_red.append(j)
        else :
            sq_blue.append(j)

    # 겹치는 부분 구하기
    for r in sq_red:
        for b in sq_blue:
            # 겹치는 영역 좌표 계산
            x1 = max(r[0], b[0])
            y1 = max(r[1], b[1])
            x2 = min(r[2], b[2])
            y2 = min(r[3], b[3])

            # 겹치는 영역이 존재하면 넓이 계산 
            if x1 <= x2 and y1 <= y2:
                area = (x2 - x1 + 1) * (y2 - y1 + 1)
                result += area

    print(f'#{Test_case} {result}')