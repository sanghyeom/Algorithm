T = int(input())

for tc in range(1,T+1):
    N = int(input())
    map_li = list(map(int,input().split()))

    i = 0
    cnt = 0
    # 인덱스 비교 변수
    max_indx = 0
    # list 내 방번호 확인 변수
    max_value = 0
    # 현재 최고 방번호 최초 인덱스
    check_p = 0
    # 돌아갈 인덱스
    check_0 = 0
    while i < N-1 :
        # 최초 인덱스 방문시 업데이트
        if max_indx < i :
            max_indx = i
            # 맥스 방번호 업데이트 
            if max_value< map_li[i]:
                # 첫시작시  
                if check_p == 0 :
                    max_value = map_li[i]
                    check_p = i
                else:
                    check_0 = check_p
                    max_value = map_li[i]
                    check_p = i

            i = map_li[check_0]
            cnt +=1
        i += 1
        cnt += 1
        if i == N - 1:
            break

    print(f'#{tc} {cnt}')