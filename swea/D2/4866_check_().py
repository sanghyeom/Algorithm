T = int(input())
for tc in range(1,T+1):
    check_word = input()
    top = -1
    stack = [0] * 51

    ans = 1
    for x in check_word:
        if x in '({[':    # 여는 괄호 push
            top += 1
            stack[top] = x
        elif x == ')':  # 닫는 괄호인 경우
            if top == -1 or stack[top] != '(' :   # 스택이 비어있으면 (여는 괄호가 없으면 )
                ans = 0
                break   # for x
            else:                 # 여는 괄호 하나 버림
                top -= 1    # pop
        elif x == '}':  # 닫는 괄호인 경우
            if top == -1 or stack[top] != '{':   # 스택이 비어있으면 (여는 괄호가 없으면 )
                ans = 0
                break   # for x
            else:           # 여는 괄호 하나 버림
                top -= 1    # pop
        elif x == ']':  # 닫는 괄호인 경우
            if top == -1 or stack[top] != '[':   # 스택이 비어있으면 (여는 괄호가 없으면 )
                ans = 0
                break   # for x
            else:           # 여는 괄호 하나 버림
                top -= 1    # pop
    if top != -1:   # 여는 괄호가 남아있으면
        ans = 0
    print(f'#{tc} {ans}')
