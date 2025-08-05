for Test_case in range(1,11):
    D = int(input())
    box_list = list(map(int,input().split())) # 충전기 위치
    box_check_list = box_list  
    result = 0     
    for i in range(D) :
        box_check_list[box_check_list.index(max(box_check_list))] = (max(box_check_list)-1)
        box_check_list[box_check_list.index(min(box_check_list))]= (min(box_check_list)+1)
        result = max(box_check_list)-min(box_check_list)

    print(F'#{Test_case} {result}')
