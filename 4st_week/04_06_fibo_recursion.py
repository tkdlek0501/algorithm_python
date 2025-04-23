input = 20

# *피보나치 수열을 재귀로 푸는 것은 비효율 적이다
# 왜냐하면 fibo(4)를 구한다 했을 때 fibo(3) + fibo(2) 를 필요로 하고
# fibo(3) 은 다시 fibo(2) + fibo(1) 을 필요로 한다
# fibo(4)와 fibo(3) 은 fibo(2) 라는 값을 공통적으로 필요로 하게 된다
# 즉 똑같은 연산을 반복하는 구조가 돼버린다
# => DP 동적 계획법을 이용해야 한다

# fibo(1) = fibo(2) = 1
# fibo(n) = fibo(n-1) + fibo(n-2)
# n번째 값을 구하기 위해서는 이전 값들의 합을 구해야 하고
# 이전 값들도 마찬가지로 그 이전 값들의 합을 알아야 한다
# *즉, 이전의 결과가 다음의 결과에 필요하니까 재귀를 쓴다
# 재귀 함수를 써야한다면 반드시 탈출 조건을 같이 생각해야 한다

def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765