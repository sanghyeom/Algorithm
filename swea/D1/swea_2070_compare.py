T = int(input())
compare = ''
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	A,B= map(int,input().split( ))
	if A>B :
		compare = '>'
	elif A==B : 
		compare = '='
	else : 
		compare ='<'

	print(f'#{test_case} {compare}')
	sum = 0
