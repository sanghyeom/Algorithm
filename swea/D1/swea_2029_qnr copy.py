T = int(input())
for test_case in range(1, T + 1):
    num1, num2 = map(int, input().split(" "))
    a = num1 // num2
    b = num1 % num2
    print(f"#{test_case} {a} {b}")
