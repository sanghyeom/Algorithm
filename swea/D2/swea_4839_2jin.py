def binarySearch(pages, key):
    start = 1
    end = pages
    count = 0

    while start <= end:
        count += 1
        mid = int((start + end) / 2)

        if mid == key:
            return count
        elif mid > key:
            end = mid 
        else:
            start = mid 

    
    return count


T = int(input())
for t in range(1, T+1):
    P, A, B = map(int, input().split())

    a_count = binarySearch(P, A)
    b_count = binarySearch(P, B)

    if a_count < b_count:
        result = 'A'
    elif a_count > b_count:
        result = 'B'
    else:
        result = '0'

    print(f"#{t} {result}")