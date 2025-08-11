T = int(input())

for tc in range(1,T+1):
    str1 = str(input())
    str2 = str(input())
    cnt = 0
    # for i in range(len(str1)) :
    for j in range(len(str2)) :
        # if str1[i] == str2[j] :
        if str2[j:j+len(str1)] == str1:
            cnt += 1
    print(f"#{tc} {cnt}")
