for tc in range(1,11):
    F = int(input())
    pan = [0]*8
    for i in range(8):
        pan[i] = list(input())
    result = 0
    for i in range(8):
        for j in range(8):
            cnt = 0
            for h in range(F):
                if 0 <= j+h < 8 and 0 <= j+F-h <= 8:
                    if pan[i][j+h] == pan[i][j+F-h-1]:
                        cnt +=1
            if cnt == F :
                result +=1
            cnt = 0
            for k in range(F):
                if 0 <= j+k < 8 and 0 <= j+F-k <= 8:
                    if pan[j+k][i] == pan[j+F-k-1][i]:
                        cnt +=1
            if cnt == F :
                result +=1
    print(f'{tc} {result}')
