T = int(input())
cal = ''
for test_case in range(1, T + 1):
	N = str(input())
	sY = N[0:4]
	sM = N[4:6]
	sD = N[6:8]
	Y = int(N[0:4])
	M = int(N[4:6])
	D = int(N[6:8])
	if M>0 and M<12 :
		if M == 1 or M ==3 or M ==5 or M ==7 or M ==8 or M ==10 or M ==12 :
			if D>0 and D<32 :
				print(f'#{test_case} {sY}/{sM}/{sD}')
		if M == 2 :
			if D>0 and D<29 :
				print(f'#{test_case} {sY}/{sM}/{sD}')
			else : 
				print(f'#{test_case} -1')
		if M == 4 or M ==6  or M ==9 or M ==11 :
			if D>0 and D<32 :
				print(f'#{test_case} {sY}/{sM}/{sD}')
	else :
		print(f'#{test_case} -1')
	