# C,R = map(int,input().split())
# K = int(input())

# if K> C  * R :
#     print(0)
#     exit()

# seats = [0] * (R+1)
# for i in range(R+1):
#     seats[i] = [0] * (C+1)

# for i in range(R):
#     for j in range(1,C+1):
#         seats[i][j] = (j,R-i)



# # 0 상 1 우 2 하 3 좌 
# direction = 0 
# nx = 1   # 1 ~ 
# ny = R - 1
# result = []
# lim_x_st = 0
# lim_y_st = 0
# lim_y = R
# lim_x = C



# for i in range(1, C*R+1):
#     print(i, nx,ny ,lim_y, lim_x, direction)
#     if i == K :
#         result = seats[ny][nx]
#         break 

#     if direction == 0 :
#         if lim_y_st<= ny-1 < lim_y :
#             ny -= 1 
#         else :
#             direction = (direction+1)%4
#             lim_y-=1
#             nx += 1 

#     elif direction == 1 :
#         if lim_x_st<= nx+1 < lim_x :
#             nx += 1 
#         else :
#             direction = (direction+1)%4
#             lim_x_st +=1
#             ny += 1 

#     elif direction ==2 :
#         if lim_y_st <= ny+1 < lim_y :
#             ny += 1 
#         else :
#             direction = (direction+1)%4
#             lim_y_st += 1
#             nx -= 1 

#     elif direction ==3 :
#         if lim_x_st<= nx-1 < lim_x :
#             nx -= 1 
#         else :
#             direction = (direction+1)%4
#             lim_x -= 1
#             ny -= 1 

# if result != [] :
#     print(*result)
# else : 
#     print(0)
        

##########################################################################

C,R = map(int,input().split())
K = int(input())

if K> C  * R :
    print(0)
    exit()

seats = [0] * (R)
visit = [0] * (R)
for i in range(R):
    seats[i] = [0] * (C)
    visit[i] = [0] * (C)
for i in range(R):
    for j in range(C):
        seats[i][j] = (j+1,R-i)
dx, dy = [0,1,0,-1],[-1,0,1,0]
direction = 0 
cnt = 1
NX = 0
NY = R-1
result = []

while cnt <= K :
    visit[NY][NX] = cnt 
    if cnt == K :
        result = seats[NY][NX]
        break
    if 0 <= NX+dx[direction] < C and 0 <= NY+dy[direction] < R and visit[NY+dy[direction]][NX+dx[direction]] == 0 : 
        NX += dx[direction]
        NY += dy[direction]
        cnt += 1 
    else : 
        direction = (direction+1)%4
print(*result)