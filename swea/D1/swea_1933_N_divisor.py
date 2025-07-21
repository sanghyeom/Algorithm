N = int(input())
listA = []

print(N)
print(type(N))

for i in range(N+1) :
    if type((N/i)) == type(N):
        print(N/i)