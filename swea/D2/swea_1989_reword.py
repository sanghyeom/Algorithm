T = int(input())
for Test_case in range(1,T+1):
    word_test = input()
    result = 1
    max_num = len(word_test)
    for i in range(max_num//2) :
        if word_test[i] != word_test[max_num - i-1]:
            result = 0


    print(f'#{Test_case} {result}')