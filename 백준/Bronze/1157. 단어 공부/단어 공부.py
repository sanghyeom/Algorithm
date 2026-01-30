word = input().upper()
cnt_word = [0]*26
for i in word :
    cnt_word[ord(i)-65]+=1

result = ''
max_num = 0
for j in range(26):
    if cnt_word[j] > max_num:
        max_num = cnt_word[j]
        result = chr(j + 65)
    elif cnt_word[j] == max_num:
        result = '?'
        
print(result)