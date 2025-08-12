T = int(input())
for tc in range(1,T+1):
    letters = list(input())
    stack = ['test']
    for i in letters : 
        if stack[-1] == i :
            stack.pop()
        else:
            stack.append(i)
    stack.remove('test')
    print(F'#{tc} {len(stack)}')