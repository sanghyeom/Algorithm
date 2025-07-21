N = input()

for i in N :
    if i == N[len(N)-1] :
        print(ord(i)-64)
    else :
        print(ord(i)-64, end=' ')
