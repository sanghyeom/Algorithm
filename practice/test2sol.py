# #  score 1 , score 2 
# # 3개 분반 
# # min <= 각 분반수 <= max
# # 3개의 분반중 가장많은 분반 - 가장 적은 분반 

# # im 최소값 : 완전 탐색 
# # 모든 경우의 수를 전부 만든다음 => 조건에 맞는것들을 검사 => 그중 최소, 최대값찾기 
# # 무식하게 전부 구하자 (brute - force)


# # 1<= 점수 <= 100
# '''
# 5
# 5 1 4
# 3 5 5 4 5 
# 6 2 6
# 5 4 4 5 5 1
# '''


# T = int(input())
# for tc in range(1, T+1):
#     N, mins, maxs = map(int, input().split())
#     scores = list(map(int, input().split()))

#     min_diff = 9999999 # 인원수 차이의 최소값.

#     for score1 in range(1, 101):
#         for score2 in range(score1, 101):
#             # (score1, score2) 가능한 모든 조합 생성 (약 1만개)

#             cls_cnt = [0]*3 
#             #cls_cnt[0] 부진
#             #cls_cnt[1] 보통
#             #cls_cnt[2] 우수

#             for score in scores:
#                 if score < score1:
#                     cls_cnt[0] += 1
#                 elif score < score2:
#                     cls_cnt[1] += 1
#                 else:
#                     cls_cnt[2] += 1
            
            
#             for i in range(3):
#                 if cls_cnt[i] < mins or cls_cnt[i] > maxs: # 만약에 세 분반중에 하나라도 범위를 벗어났다면
#                     break # 멈추기
#             else: # for문을 돌면서 break 안만난 상황
#                 # 세 반 모두 다 범위 안에 있음. 여기서 검사
#                 # 세 분반의 최대 인원 - 최소 인원
#                 max_cnt = 0
#                 min_cnt = 9999999
#                 for i in range(3):
#                     if cls_cnt[i] > max_cnt:
#                         max_cnt = cls_cnt[i]
#                     if cls_cnt[i] < min_cnt:
#                         min_cnt = cls_cnt[i]
#                 diff = max_cnt - min_cnt
#                 if diff < min_diff:
#                     min_diff = diff
    
#     if min_diff == 9999999:
#         print(f"#{tc} -1")
#     else:
#         print(f"#{tc} {min_diff}")

# #------------------------------------------------------------------
# # counting 배열 확인



TC = int(input())

for t in range(1, TC+1):
    N, MIN, MAX = map(int, input().split())
    scores = list(map(int, input().split()))

    good = []
    normal = []
    bad = []

    minus = 0
    score1 = max(scores)
    score2 = max(x for x in scores if x < score1)
    # for i in scores:
    #     if i < score1:
    #         s = i
    #         if s > score2:
    #             score2 = s

    for i in range(N):
        if scores[i] >= score1:  
            good.append(scores[i])

        elif score2 <= scores[i] < score1 :
            normal.append(scores[i])

        elif scores[i] < score2:
            bad.append(scores[i])
    
    if MIN <= len(good) <= MAX and MIN <= len(normal) <= MAX  and MIN <= len(bad) <= MAX :
        minus = max(len(good), len(normal), len(bad)) - min(len(good), len(normal), len(bad))
        
    else:
        minus = -1
    print(f'#{t} {minus}')