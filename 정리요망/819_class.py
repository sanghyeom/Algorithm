def f(i,N, s) : # bit[i]를 결정하는 함수, i-1 원소까지 결정된 부분집합의 합 s 
    global cnt
    global fcnt
    fcnt += 1
    if s == key :   # 부분집합의 합이 찾는 값인 경우
        cnt +=1
    elif s > key :
        return
    elif i == N :     # 더이상 남은 원소가 없는 경우 
        return 
        # s = 0
        # for i in range(N):
        #     if bit[i]:
        #         s += A[i]
        # if s == key :
        #     cnt+=1
    else :
        bit[i] = 1          # A[i] 포함
        f(i+1,N ,s+ A[i])
        bit[i] = 0             # A[i] 미포함
        f(i+1,N, s)

N = 10 
A = [i for i in range(1, N+1)]

key = 10
cnt = 0 
fcnt = 0
bit = [0] *N
f(0,N, 0)
print(cnt, fcnt)