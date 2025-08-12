# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

top = -1
stack = [0] * 10 

top+=1 # push(1)
stack[top] = 1
top+=1 # push(2)
stack[top] = 2
top+=1 # push(3)
stack[top] = 3

top-=1  # pop()
print (stack[top+1])
top-=1  # pop()
print (stack[top+1])
top-=1  # pop()
print (stack[top+1])

print(stack) # 이것만가지곤 원소가남았는지 알수없음 , top을 확인할것. 
