# Q. N으로 표현
#
# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
#
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
#
# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.
# 입출력 예
# N	number	return
# 5	12	4
# 2	11	3


# <문제분석>
# 5와 사칙연산 만으로 12 표현 (55, 555, .. 가능)
# 숫자 N과 number 주어질 때 사칙연산으로 표현할 수 있는 방법 중
# N의 사용횟수의 최솟값을 return 하도록 해야한다

# 1 <= N <= 9
# number 는 32,000 이하
# 괄호와 사칙연산 가능, 나누기 연산에서 나머지 무시
# 최솟값이 8보다 크면 -1 을 return

# <풀이>
# 5를 어떻게 활용해야 하는지..
# 어떤 사칙 연산을 해야 하는지 아무것도 구할 수 없다


def solution(N, number):
    if N == number:
        return 1

    # 최솟값이 8보다 크면 -1 return 해야 하므로
    dp = [set() for _ in range(9)]  # dp[1] ~ dp[8]까지 사용

    for i in range(1, 9): # 1 ~ 8
        # N을 i번 연속 사용한 수 (예: 5, 55, 555 등)
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if number in dp[i]:
            return i

    return -1