N = list(map(int,input().split()))
M = 1000000
COUNTS = [0] *(M+1)
TEMP = [0] *(M+1)
# COUNTS = [0] * M
for i in range(len(N)) :
    COUNTS[N[i]] += 1

for i in range(1,M+1) :
    COUNTS[i] += COUNTS[i-1]

for i in range(len(N)-1,-1,-1):
    COUNTS[N[i]]-=1
    TEMP[COUNTS[N[i]]] = N[i]

print(TEMP[500000])