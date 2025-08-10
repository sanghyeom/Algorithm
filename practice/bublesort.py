N = [9,4,3,2,1,5,6,7,5,2,1,1]

for j in range(1,len(N)):
    for i in range(len(N)-j):
        if N[i]>N[i+1] :
            temp = N[i]
            N[i] = N[i+1] 
            N[i+1]= temp 

print(N)