N = int(input())
total = 0

for i in range(1,5):
    total += N//10**(4-i)
    N = N-(N//10**(4-i))*10**(4-i)
print(total)
