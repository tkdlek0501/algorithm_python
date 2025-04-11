# 아이디어
# 현재의 n과 새로 들어오는 n-1을 계속 곱하다가
# 새로들어오는 값이 1이 되면 결과를 return 한다

# ex.
# 5, 4, 3, 2, 1
# 5 -> 20 -> 60 -> 120
# factorial(n) = n * factorial(n-1)
# factorial(n-1) = (n-1) * factorial(n-2)

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)



print(factorial(5))