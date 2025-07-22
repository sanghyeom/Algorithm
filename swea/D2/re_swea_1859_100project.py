T = int(input())

for Test_case in range(1,T+1) :
    N = int(input())
    sale = list(map(int,input().split()))
    min = 0
    max = 0
    money = 0
    count =0
    s_sale = sorted(sale)
    s_total = 0
    for a in range(N-1):
        s_total += int(s_sale[a])
    if s_sale[N-1] > s_total :
        money = int(s_sale[N-1]*(N-1))-s_total
        print(f'#{Test_case} {money}')
    else : 
        for i in range(N):
            if i == (N-1) :
                money += int(max*count)-int(min)
                print(f'#{Test_case} {money}')
            elif sale[i]<=sale[i+1]:
                count += 1
                min += sale[i]
                max = sale[i+1]
            elif sale[i]>sale[i+1]:
                money += int(max*count)-int(min)
                count = 0
                max = 0
                min = 0
    
    ########################################################
def gpt(): 
    T = int(input())
    for Test_case in range(1, T + 1):
        N = int(input())
        sale = list(map(int, input().split()))

        max_price = 0
        profit = 0

        for price in reversed(sale):
            if price > max_price:
                max_price = price
            else:
                profit += max_price - price

        print(f'#{Test_case} {profit}')