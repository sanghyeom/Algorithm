import copy
T = int(input())

for Test_case in range(1,T+1):
    N = int(input())
    NC = copy.deepcopy(N)
    i = 1
    sol = {0,1,2,3,4,5,6,7,8,9}
    nums = []
    while sol!=set(nums) : 
        if N>1000 :
            N = i * NC
            nums.append(N%10)
            N=N-N%10 
            nums.append(int(N%100/10))
            N=N-N%100
            nums.append(int(N%1000/100))
            N=N-N%1000
            nums.append(int(N%10000/1000))
            N=N-N%10000
            i = i+1
        elif 1000>=N>100 :
            N = i * NC
            nums.append(N%10)
            N=N-N%10 
            nums.append(int(N%100/10))
            N=N-N%100
            nums.append(int(N%1000/100))
            N=N-N%1000
            i = i+1
        elif 100>=N>10 :
            N = i * NC
            nums.append(N%10)
            N=N-N%10 
            nums.append(int(N%100/10))
            N=N-N%100
            i = i+1 
        elif 10>=N>0 :
            N = i * NC
            nums.append(N%10)
            N=N-N%10 
            i = i+1
            
    print(f'#{Test_case} {i*NC}')