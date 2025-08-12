# T = int(input())

# for tc in range(1,T+1) : 
#     A,B = map(str, input().split())
#     cnt =0
#     position = 0
#     for i in range(len(A)):
#         if A[i:i+len(B)] == B :
#             cnt +=1
#             position = i+len(B)
#         elif i < position :
#             continue
#         else:
#             cnt +=1

#     print(f'#{tc} {cnt}')
# -------------------------------------------

T = int(input())

for tc in range(1,T+1) : 
    A,B = map(str, input().split())
    cnt =0
    position = 0
    while position < len(A) :
        if A[position:position+len(B)] == B :
            cnt +=1
            position += len(B)

        else:
            cnt +=1
            position +=1
    print(f'#{tc} {cnt}')