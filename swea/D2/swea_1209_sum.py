T = int(input())
for Test_case in range(1,T+1):
    
    # 스도쿠 업로드
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int,input().split())))
    
    # 정답 검증 result
    result =1 
    for i in range(9):
        sum_y = 0
        for j in range(9):
            sum_y += sudoku[j][i]
            if (i%3) == 0 and (j%3) == 0 :
                sum_nine = 0
                for x in range(0,3):
                    for y in range(0,3):
                        sum_nine += sudoku[i+x][j+y]
                if sum_nine != 45 : 
                    # print('칸 문제')
                    result = 0 
        
        if sum(sudoku[i]) != 45 :
            result = 0 
            # print('가로줄 문제')
        if sum_y != 45 : 
            result = 0 
            # print('세로줄 문제')



    print(f'#{Test_case} {result}')