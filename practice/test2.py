'''
봉사 동아리 N 명 대상 교육 
세개의 반 우수 보통 부진 
미리 제출한 score1 , score2를 임의로 선정
score2 이상 우수 
score1~ 2 보통
score1 미만 부진 

최소인원 min 이상 최대인원 max 이하 만족 
가장많은분반과 적은 분반의 학생수 차의 최속값 ? 
만약 조건 을 만족하지않으면 -1 을 ! 
T
N min max 
n1 n2 n3 . . . .

5
5 1 4
3 5 5 4 5 
6 2 6
5 4 4 5 5 1

'''

T = int(input())
for tc in range(1,T+1) :
    N , mins , maxs = map(int,input().split())
    student_li = list(map(int,input().split()))
    # 최대 최소 스코어 확인
    mins_score = 100
    maxs_score = 1
    student_class = []
    gap = N
    max_class = 0
    min_class = N
    
    for i in student_li :
        if i > maxs_score : 
            maxs_score = i 
        if i < mins_score : 
            mins_score = i +int(1)
    # 클래스별 인구수 


    # 분반
    def test_class(): 
        global mins_score
        global maxs_score
        global student_class
        class_A = 0
        class_B = 0
        class_C = 0
        for i in range(N) :
            if student_li[i] >= maxs_score :
                class_A += 1
            elif student_li[i] < mins_score :
                class_C += 1
            else : 
                class_B += 1
        student_class = [class_A,class_B,class_C]

    # 누가 젤 많고 , 누가 젤 적은지 ? 
    def how_many() :
        global student_class 
        global gap
        global max_class 
        global min_class 
        global mins

        for i in range(3):      
            if  max_class < student_class[i] :
                max_class = student_class[i] 
            elif  min_class > student_class[i] :
                min_class = student_class[i] 
        if min_class < mins: 
            mins_score += 1
        

        gap = max_class - min_class
    
    # 최소인원 맞추기
    # def check_min_max():
    #     global maxs
    #     global mins
    #     global max_class
    #     global min_class
    #     global maxs_score
    #     global mins_score
        
    #     if min_class < mins : 
    #         mins_score += 1

    #     if max_class > maxs : 
    #         maxs_score -= 1


    

    test_class()
    how_many()

    
    print(f'#{tc} {gap} {student_class}')
