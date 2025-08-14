'''
(6+5*(2-8)/2)
6528-*2/+
'''

stack = [0]*100
top = -1

icp = {'(':3,'*':2,'/':2,'+':1,'-':1} # 밖에 있을때 의 우선순위  (클수록높음)
isp = {'(':0,'*':2,'/':2,'+':1,'-':1} # 스택안에 있을때의 우선순위 (클수록높음)

infix = '(6+5*(2-8)/2)'
postfix = ''   # 여기 저장할 예정.

for token in infix : 
    if token not in '(+-*/)'# 피 연산자 이면 후위식에 추가
        postfix += token
    elif token == ')' #여는 괄호를 만날떄 까지 pop 
        while top> -1 and stack[top]!= '(' :
            top -= 1
            postfix += stack[top+1]
        if top != -1 :
            top -= 1   #  '(' 버림
    else :               # 연산자인경우
        if top == -1 or isp[stack[top]]< icp[token] # 토큰의 우선순위가 더 높으면
            top += 1 # push
            stack[top]= token
        elif isp[stack[top]] >= icp[token] # 토큰과 같거나 더 높으면
            while top> -1 and isp[stack[top]] >= icp[token] :
                top -= 1
                postfix += stack[top+1]
            top += 1   # push
            stack[top] = token
    print(postfix, stack)