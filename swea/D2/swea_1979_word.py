T = int(input())
for Test_case in range(1,T+1):
    N, K = map(int,input().split())
    # 단어판 업로드
    word = []
    for _ in range(N):
        word.append(list(map(int,input().split())))
    
    # 정답 검증 result
    result = 0
    
    for i in range(N):
        for j in range(N):
            if word[i][j] == 1 :
                if j>=1 and word[i][j-1] == 1 :
                    if sum(word[i][j:j+K])==K : 
                        result -= 1
                if j+K <= N :
                    if sum(word[i][j:j+K])==K : 
                        result += 1
                        if j+K+1 <= N and sum(word[i][j:j+K+1])>K : 
                            result -= 1
               
            if word[j][i] == 1 :
                if j>=1 and word[j-1][i] ==1 :
                    if j>=1 and word[j-1][i] ==1 :
                        if j+K <= N and sum(word[x][i] for x in range(j, j+K)) == K:
                            result -= 1
                if j+K <= N :
                    if sum(word[x][i] for x in range(j, j+K)) == K:

                        result += 1
                        if j+K+1 <= N and sum(word[x][i] for x in range(j, j+K+1)) > K:
                            result -= 1


    print(f'#{Test_case} {result}')