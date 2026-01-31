N = int(input())
swich_num = list(map(int,input().split()))
student_N = int(input())

def swich_changer(idx) :
    global swich_num
    if swich_num[idx] == 0 :
        swich_num[idx] = 1
    else :
        swich_num[idx] = 0

for i in range(student_N): 
    S , num = map(int,input().split())
    if S == 1 :
        for j in range(1,N+1):
            if j % num == 0 :
                swich_changer(j-1)
    else :
        center = num-1
        cnt = 0
        swich_changer(center)
        while True:
            cnt +=1
            if 0<=center+cnt<N and 0<=center-cnt<N and swich_num[center+cnt] == swich_num[center-cnt] :
                swich_changer(center+cnt)
                swich_changer(center-cnt)
            else:
                break


for i in range(0, N, 20):
    print(*swich_num[i:i+20])
