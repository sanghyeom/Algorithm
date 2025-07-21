N = input()
A= []
for i in N :
    if ord(i)>=97 : 
        A.append(chr(ord(i)-32))
    else :
        A.append(i)
for j in range(len(N)) :
    if j == len(N)-1 :
        print(A[j])
    else:
        print(A[j],end='')