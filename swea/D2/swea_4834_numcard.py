T = int(input())

for Test_case in range(1,T+1):
    N = int(input())
    ai = input()
    counts = [0]*10
    for i in ai :
        num = int(i)
        counts[num] += 1
    check_same = 0
    max_num = counts.index(max(counts))
    for j in range(len(counts)):
        if check_same < counts[j] :
            check_same = counts[j]  
        if counts[j] == check_same :
            max_num = j

    print(f'#{Test_case} {max_num} {max(counts)}')
     