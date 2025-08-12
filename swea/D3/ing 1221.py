T = int(input())

for tc in range(1,T+1):
    m,n = map(str,input().split())
    n = int(n)
    test_len = list(map(str,input().split()))

    counting_len = [0]*10
    result_len = [0]*n
    for i in range(n):
        if test_len[i] == 'ZRO' :
            counting_len[0] += 1
        elif test_len[i] == 'ONE' :
            counting_len[1] += 1
        elif test_len[i] == 'TWO' : 
            counting_len[2] += 1
        elif test_len[i] == 'THR' :
            counting_len[3] += 1
        elif test_len[i] == 'FOR' : 
            counting_len[4] += 1
        elif test_len[i] == 'FIV' :
            counting_len[5] += 1
        elif test_len[i] == 'SIX' : 
            counting_len[6] += 1
        elif test_len[i] == 'SVN' :
            counting_len[7] += 1
        elif test_len[i] == 'EGT' : 
            counting_len[8] += 1
        elif test_len[i] == 'NIN' :
            counting_len[9] += 1
    for j in range(1,len(counting_len)):
        counting_len[j]+= counting_len[j-1]

    for x in range(len(test_len)-1,-1,-1):
        result_len[counting_len[x]]=test_len[x]
        if test_len[x] == 'ZRO' :
            counting_len[0] -= 1
        elif test_len[x] == 'ONE' :
            counting_len[1] -= 1
        elif test_len[x] == 'TWO' : 
            counting_len[2] -= 1
        elif test_len[x] == 'THR' :
            counting_len[3] -= 1
        elif test_len[x] == 'FOR' : 
            counting_len[4] -= 1
        elif test_len[x] == 'FIV' :
            counting_len[5] -= 1
        elif test_len[x] == 'SIX' : 
            counting_len[6] -= 1
        elif test_len[x] == 'SVN' :
            counting_len[7] -= 1
        elif test_len[x] == 'EGT' : 
            counting_len[8] -= 1
        elif test_len[x] == 'NIN' :
            counting_len[9] -= 1


    print(result_len)
