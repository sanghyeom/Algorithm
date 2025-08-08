# T = int(input())
# 버블 정렬 구현 
# for Test_case in range(1,T+1):
#     N = int(input())
#     N_lis = list(map(int,input().split()))
#     temp=0
#     for j in range(1,N):
#         for i in range(N-j): 
#             if N_lis[i] > N_lis[i+1]:
#                 temp = N_lis[i] 
#                 N_lis[i] = N_lis[i+1]
#                 N_lis[i+1] = temp

#     print(f"#{Test_case} {' '.join(map(str,N_lis))}")

# # 카운팅 
# for Test_case in range(1,T+1):
#     N = int(input())
#     N_lis = list(map(int,input().split()))
#     max_val =0
#     for num in N_lis:
#         if max_val < num:
#             max_val = num
#     counted = [0]*(max_val+1)
#     counted_N_lis = []

#     for h in range(N) :
#         counted[N_lis[h]] +=1

#     for i in range(1,N+1):
#         counted[i] += counted[i-1]
    
#     # for j in range (N-1,-1,-1):
#     #     counted[N_lis[j]]  -= 1
#     #     counted_N_lis[counted[N_lis[j]]] = N_lis[j]




#     # print(f"#{Test_case} {' '.join(map(str,N_lis))}")
#     print(*counted)


# # 선택

# T = int(input())

# for t in range(1, T+1):
#     P, A, B = map(int, input().split())
#     p_list = list(range(P+1))

#     def binarySearch(arr, N, key):
#         start = 1
#         bi_cnt = 0
#         end = N-1
#         while start <= end:
#             bi_cnt +=1   
#             middle = (start + end) // 2
#             if arr[middle] == key:      
#                 return bi_cnt # 반환 목적이 위치가 아니라 카운트 횟수이기 때문에 카운트 반환                       
#             elif arr[middle] > key:
#                 end = middle -1    
#             else:                  
#                 start = middle + 1 
#         return -1
            
#     a = binarySearch(p_list, P, A)
#     b = binarySearch(p_list, P, B)
#     if a < b:
#         print(f"#{t} A")
#     elif a > b:
#         print(f"#{t} B")
#     else:
#         print(f"#{t} 0")



    
# T = int(input())

# for t in range(1, T+1):
#     P, A, B = map(int, input().split())

#     def binarySearch(pages, key):
#         start = 1
#         end = pages
#         count = 0

#         while start <= end:
#             count += 1
#             mid = int((start + end) / 2)

#             if mid == key:
#                 return count
#             elif mid > key:
#                 end = mid 
#             else:
#                 start = mid 

        
#         return count

#     a_count = binarySearch(P, A)
#     b_count = binarySearch(P, B)

#     if a_count < b_count:
#         result = 'A'
#     elif a_count > b_count:
#         result = 'B'
#     else:
#         result = '0'

#     print(f"#{t} {result}")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_list = list(map(int, input().split()))
    for i in range(N//2):  # N범위 절반만 탐색
        min_idx = i
        max_idx = i
        for j in range(i , N-i):  # 변환된 맨앞뒤 영역 건들지 않기 위해
            if input_list[min_idx] > input_list[j]:
                min_idx = j
            if input_list[max_idx] < input_list[j]:
                max_idx = j
        input_list[i], input_list[min_idx] = input_list[min_idx], input_list[i]
        # if max_idx == i :          # 만약 min, max가 같은위치를 참고한다면 바뀌어진 min위치 참조
        #     max_idx = min_idx
        input_list[N-1-i], input_list[max_idx] = input_list[max_idx], input_list[N-1-i]
    print(input_list)