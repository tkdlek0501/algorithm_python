input = 100

# DP는
# 결과를 기록하여 추후 재사용할 때 효율적으로 꺼낼 쓸 수 있게 하는 방식이다
# -> 결과를 기록하는 것 = 메모이제이션
# 단, 제약 조건이 있다. 문제를 쪼갤 수 있는 구조인 '겹치는 부분 문제' 일 때만 사용 가능하다
# ex. 기록이 추후 재사용하지 않는 케이스라면 사용 의미가 없다

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# 1. 메모에 이미 해당 값이 있으면 반환한다
# 2. 만약 없다면, 그 값을 피보나치를 통해 구하고 메모에 저장한다

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo

print(fibo_dynamic_programming(input, memo))