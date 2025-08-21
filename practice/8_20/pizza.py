T = int(input())

for tc in range(1,T+1):
    N, M  = map(int,input().split())
    # 화덕크기 N , 피자개수 M
    Ci = list(map(int,input().split()))

    result = 0

    cq = [0] * (N+1) 
    front = rear = 0

    def is_full():
        return (rear+1) % len(cq) == front

    def is_empty():
        return front == rear

    def enqueue(item) : 
        global rear 
        if is_full() :
            print('Queue_Full')
        else :
            rear = (rear +1) % len(cq)
            cq[rear] = item 
    def dequeue():
        global front
        if is_empty():
            print('Queue_EMpty')
        else:
            front = (front+1) % len(cq)
            return cq[front]
    
    idx = 0 
    
    while True :
        if cq[(front+1) % len(cq)] == 0 and idx < M :
            dequeue()
        
        if is_full() == False :
            enqueue(Ci[idx])
            if idx < M : 
                idx +=1
        else :
            enqueue(dequeue()//2)
        
            
        
        

        if idx == M and max(cq) <= 1 :
            break
        print(cq)
    
        
    print(f'#{tc} {result}')
        