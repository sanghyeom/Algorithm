N = [9,4,3,2,1,5,6,7,5,2,1,1]

min_value = N[0]

for i in range(len(N)-1):
    for j in range(i+1,len(N)):
        if N[j] < N[min_value] :
            min_value =j
    N[i],N[min_value] =N[min_value],N[i]


print(N)