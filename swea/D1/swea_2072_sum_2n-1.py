T = int(input())
sum = 0
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	N=list( map(int,input().split( )))
	for i in N:
		if i%2 == 1:
			sum += i
	print(f'#{test_case} {sum}')
	sum = 0
