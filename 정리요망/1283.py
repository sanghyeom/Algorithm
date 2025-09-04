N = int(input())
lst_word = [0] * N
for i in range(N) :
    lst_word[i] = input()
check_lst = []

def check_LU(i,j):
    global lst_word
    global check_lst

    if lst_word[i][j] not in check_lst :
        check_lst.append(lst_word[i][j].lower())
        check_lst.append(lst_word[i][j].upper())
        if j == 0 : 
            lst_word[i] = '['+lst_word[i][j]+']'+lst_word[i][1:]
        else : 
            lst_word[i] = lst_word[i][0:j]+'['+lst_word[i][j]+']'+lst_word[i][j+1:]
    else : 
        check_LU(i,j+1)



def check_LU2(i,j,k):
    global lst_word
    global check_lst

    A,B=lst_word[i].split()
    temp_word = [A,B]
    
    if k == 'a' :
        if A[j] not in check_lst :
            check_lst.append(A[j].lower())
            check_lst.append(A[j].upper())
            if j == 0 : 
                temp_word[0] = '['+A[j]+']'+A[1:]
            else : 
                temp_word[0] = A[0:j]+'['+A[j]+']'+A[j+1:]
        else : 
            return check_LU2(i,j,'b')

    elif k == 'b' : 
        if B[j] not in check_lst :
            check_lst.append(B[j].lower())
            check_lst.append(B[j].upper())
            if j == 0 : 
                temp_word[1] = '['+B[j]+']'+B[1:]
            else : 
                temp_word[1] = B[0:j]+'['+B[j]+']'+B[j+1:]
            return temp_word
        else : 
            j+=1 
            return check_LU2(i,j,'a')
            
    return temp_word

            


for i in range(N):
    if lst_word[i].count(' ') != 1 :
        check_LU(i,0)
    else : 
        lst_word[i] = ' '.join(check_LU2(i,0,'a'))
        
print(lst_word)