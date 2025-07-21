N = int(input())
listA = []

for i  in range(N+1) :
    revers = N-i
    if revers == 0 :
        pass
    elif N%revers == 0 :
        print(int(N/revers),end=" ")