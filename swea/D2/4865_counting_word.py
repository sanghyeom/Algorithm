T = int(input())

for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    counting_max_num = 0
    counting_num = 0
    for i in str1:
        counting_num = 0
        for j in str2 :
            if j == i : 
                counting_num +=1
        if counting_max_num< counting_num :
            counting_max_num = counting_num
    print(f'#{tc} {counting_max_num}')

