# Q. 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12931

# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
#
# 제한사항
# N의 범위 : 100,000,000 이하의 자연수
# 입출력 예
# N	answer
# 123	6
# 987	24
# 입출력 예 설명
# 입출력 예 #1
# 문제의 예시와 같습니다.
#
# 입출력 예 #2
# 9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.

# <문제분석>
# 자연수 N에 대해 각 자릿수의 합을 구해서 return
# ex. N = 123 이면 1 + 2 + 3 = 6 return
# N은 100,000,000 이하의 자연수 -> 이중 for문 쓰면 안됨

# <구현>
# ex 123 에 대해서
# 1. 먼저 N의 자릿수가 몇인지 길이를 재야 한다
# 2. 반복문 돌면서 나눈 몫을 더해준다 그리고 자릿수 감소, N의 값에서 빼줌
# 100 으로 나누면 -> 1
# 10으로 나누면 -> 12 => 이미 나눠진 값에 대해서는 빼준다?
# 1 로 나누면 -> 123

n = 123 # 6

# def solution(n):
#     answer = 0
#
#     digit_count = len(str(n))  # 총 자릿수
#
#     for i in range(digit_count - 1, -1, -1):
#         num = n // (10 ** i)  # 현재 자릿 값
#         n -= num * (10 ** i)
#         answer += num  # 합
#
#     return answer
#
# print(solution(n))

# 더 좋은 방법
def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10  # 마지막 자릿수 더하기
        n //= 10  # 마지막 자릿수 없애기 (한 자릿수 줄이기)

    return answer
