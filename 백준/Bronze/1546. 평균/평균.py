N =int(input())
sum_N = 0 
li_N = list(map(int,input().split()))
max_N = max(li_N)
result = 0
for i in li_N :
    result += i / max_N *100
result = result/N
print(result)