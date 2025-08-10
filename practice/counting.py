N = [9,4,3,2,1,5,6,7,5,2,1,1]

countingli = [0]*(len(N)+1)
re_N=[0]*len(N)

for j in N:
    countingli[j] +=1

for i in range(1,len(countingli)):
    countingli[i]+= countingli[i-1]
for i in range(len(N)-1,-1,-1):
    index_num = countingli[N[i]]-1
    re_N[index_num] = N[i]
    countingli[N[i]]-=1
print(re_N)