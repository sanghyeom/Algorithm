T= int(input())

for tc in range(1,T+1):
    N = int(input())
    lis = str(input())
    max_cnt= 0
    cnt =0
    for i in range(N) :
        if lis[i] == '1':
            cnt +=1 
        elif lis[i] == '0':
            cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt

    print(f"#{tc} {max_cnt}")

for d in datas:
    if d == 0:
        cnt = 0
    elif d == 1:
        cnt += 1
    
    if max_val < cnt:
        max_val = cnt

print(f'#{t} {max_val}')