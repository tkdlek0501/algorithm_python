# Q. 두 정수 사이의 합
# 문제 설명
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
#
# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.
# 입출력 예
# a	b	return
# 3	5	12
# 3	3	3
# 5	3	12

# <문제분석>
# a와 b 정수 사이에 속한 모든 정수의 합 출력
# ex. a = 3, b = 5 이면 3 + 4 + 5 = 12 출력

# if a == b 이면 아무 수나 return
# 대소관계는 정해져 있지 않다

# <풀이>

def solution(a, b):
    answer = 0

    if a == b:
        return a

    if a < b:
        for i in range(a, b + 1):
            answer += i
    else:
        for i in range(b, a + 1):
            answer += i

    return answer

# <피드백>
# 어떤 수가 더 큰지 알 수 있는 방법은
# 위 처럼 비교 or min, max를 활용하는 방법이 있다
# 비교 후 두 수를 바꾼다던지
def adder1(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

# min, max 를 활용한다던지
def adder2(a, b):
    return sum(range(min(a, b), max(a, b)+1))