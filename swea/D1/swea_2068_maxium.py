T = int(input())
MAX = 0
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	N =list( map(int,input().split()))
	for i in range(len(N)-1):
		if MAX <= N[i+1] :
			MAX =  N[i+1]
		else:
			MAX = MAX
	print(f'#{test_case} {MAX}')
	MAX = 0
