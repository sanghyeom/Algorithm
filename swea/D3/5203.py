T = int(input())
for TC in range(1,T+1):
    lst = list(map(int,input().split()))
    play_1 = [0] * 10 
    play_2 = [0] * 10 
    result = 0
    def find_3num(player_num):
        global result 
        if player_num == 1 :
            for i in range(10):
                if play_1[i] >= 3 : 
                    result = 1
                    return result
        else : 
            for i in range(10):
                if play_2[i] >= 3 : 
                    result = 2
                    return result
        return result

    def find_strate(player_num) :
        global result 
        cnt = 0 
        if player_num == 1 :
            for i in range(10):
                if play_1[i] != 0 :
                    cnt +=1
                    if cnt >=3 : 
                        result = 1
                        return result
                else :
                    cnt =0 
        else : 
            for i in range(10):
                if play_2[i] != 0 :
                    cnt +=1
                    if cnt >=3 : 
                        result = 2
                        return result
                else :
                    cnt =0 
        return result

    for i in range(12):
        if i % 2 == 0 : 
            play_1[lst[i]] +=1  
        else : 
            play_2[lst[i]] +=1  

        result = find_3num(1)
        if result != 0 :
            break
        result = find_3num(2)
        if result != 0 :
            break
        result = find_strate(1)
        if result != 0 :
            break
        result = find_strate(2)
        if result != 0 :
            break

    print(f'#{TC}',result)