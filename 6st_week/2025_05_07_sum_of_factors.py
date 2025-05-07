# Q. 약수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/12928

# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
#
# 제한 사항
# n은 0 이상 3000이하인 정수입니다.
# 입출력 예
# n	return
# 12	28
# 5	6
# 입출력 예 설명
# 입출력 예 #1
# 12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.
#
# 입출력 예 #2
# 5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.


# <문제분석>
# 정수 n 을 입력 받아 n의 약수를 모두 더한 값을 return 해야 한다
# 0 <= n <= 3,000 인 정수

# <문제풀이>
# 약수의 개념 : 1을 포함하여 자기 자신까지 정확히 나누어 떨어지는 수 (나머지가 없어야 됨)

n = 12 # 28
# n = 5 # 6

def solution(n):
    answer = 0

    for num in range(1, n + 1):
        if n % num == 0:  # 나누어 떨어지는 수 = 약수
            answer += num

    return answer

print(solution(n)) # 28

# 더 좋은 방법
# O(n) -> O(√n)
# def solution(n):
#     answer = 0
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             answer += i
#             if i != n // i:
#                 answer += n // i
#     return answer