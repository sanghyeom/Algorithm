T = int(input())
for TC in range(1,T+1):
    N = int(input())
    pan = [ list(map(int,input().split())) for _ in range(N)]

    minimum = 99999999999999
    selected = [] 
    sum_value = 0 

    def check_pan(num) : 
        global selected
        global sum_value
        global minimum

        if sum_value >= minimum:
            return
        if len(selected)==N :
            minimum = min(minimum,sum_value)
            return
        
        for i in range(N):
            if i not in selected :
                selected.append(i)
                sum_value += pan[num][i]
                check_pan(num+1)
                sum_value -= pan[num][i]
                selected.pop()

    check_pan(0)

    print(f'#{TC}',minimum)