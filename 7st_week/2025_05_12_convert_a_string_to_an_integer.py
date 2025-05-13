# Q. 문자열을 정수로 바꾸기
# 문제 설명
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
#
# 제한 조건
# s의 길이는 1 이상 5이하입니다.
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다.
# s는 "0"으로 시작하지 않습니다.
# 입출력 예
# 예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.


# <문제분석>
# 문자열 s를 숫자로 변환해야함
# s의 길이는 1 이상 5이하
# s는 부호(+, -) 와 숫자로만 이루어져 있음
# s는 0으로 시작하지 않음

# <구현>
# str이 "1234" -> 1234
# str이 "-1234" -> -1234


# def solution(s):
#     answer = 0
#
#     for i in range(1, len(s) + 1):  # "1234" (0 ~ 3)
#         character = s[-i]
#         if character == '-':
#             answer *= -1
#         elif character == '+':
#             continue
#         else:
#             answer += int(character) * (10 ** (i - 1))
#
#     return answer

# <피드백>
# 어렵게 풀 이유가 없다
# int(str) 을 통해 변환하면 부호는 자동으로 인식하여 변환해준다

def strToInt(str):
    result = int(str)
    return result