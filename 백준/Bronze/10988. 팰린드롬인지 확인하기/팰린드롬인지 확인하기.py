word = input()
result = 1
for idx in range(len(word)//2):
    if word[idx] != word[(len(word)-idx-1)] :
        result = 0
        break
print(result)