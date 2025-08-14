T = int(input())

for tc in range(1,T+1):
    test_code = list(map(str,input().split()))
    stack = [0]*len(test_code)
    top = -1 
    result = 0
    for i in test_code :
        if i in '+/-*':
            if  top < 1:
                result = 'error'
                break
            else : 
                a = stack[top-1]
                b = stack[top]
                top -= 1
                if i == '+':
                    stack[top] = a + b
                if i == '*':
                    stack[top] = a * b
                if i == '-':
                    stack[top] = a - b
                if i == '/':
                    stack[top] = int(a / b)

        elif i == '.' :
            if top == 0:
                result = stack[top]
            else:
                result = 'error'
                break

        
        else :
            top += 1 
            stack[top] = int(i)
    print(f'#{tc} {result}')
