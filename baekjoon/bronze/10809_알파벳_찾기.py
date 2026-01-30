word = input()

result = [-1] * 26

for i in range(len(word)) :
    idx = ord(word[i]) - ord('a')
    if result[idx] == -1 :
        result[idx] = i 

print(*result)