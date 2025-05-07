# Q. 자연수 뒤집어 배열로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12932

# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
#
# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	return
# 12345	[5,4,3,2,1]

# <문제 분석>
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 return
# n이 12345 이면 마지막 숫자부터 넣어줘서 5, 4, 3, 2, 1

# <구현>

def solution(n):
    answer = []

    while n > 0:
        answer.append(n % 10)  # 나머지 = 맨 끝자리
        n //= 10  # 마지막 자리 제거

    return answer