# T = int(input())
# for TC in range(1,T+1):
#     N = int(input())
#     lst_cost = list(map(int,input().split()))
#     result = 0 
#     cost_buy = 0
#     cnt_buy = 0 
#     while lst_cost :
#         M = max(lst_cost) 
#         if lst_cost[0] == M :
#             result += lst_cost.pop(0)*cnt_buy - cost_buy
#             cost_buy = 0
#             cnt_buy = 0 
#         else : 
#             cost_buy += lst_cost.pop(0)
#             cnt_buy += 1

#     print(f'#{TC}',result)

# =--------------------------------------------

T = int(input())
for TC in range(1,T+1):
    N = int(input())
    lst_cost = list(map(int,input().split()))
    result = 0 
    cost_buy = 0
    cnt_buy = 0 
    S = 0 
    lst_cost.remove(0:2)
    print(lst_cost)
    # e = 
    # while lst_cost :
    #     M = max(lst_cost) 
    #     A = lst_cost.index(M)
    #     result+= sum(lst_cost[0:A])
    #     print(result)
    # # print(f'#{TC}',result)