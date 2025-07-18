# Q. 짝지어 제거하기

# <문제분석>
# 알파벳 소문자로 이루어진 문자열
# 1. 같은 알파벳이 2개 붙어 있는 짝 찾고
# 2. 그 둘을 제거한 뒤
# 3. 앞뒤로 문자열을 이어 붙인다
# 과정 반복해서 모두 제거한다면 종료

# <풀이>
# 길이 1,000,000 이하 -> 1회 순회 가능
# S를 짝지어 제거하기를 성공적으로 수행할 수 있는지여부 반환 1 or 0
# ex. baabaa
# b aa baa
# bb aa
# aa
#
# 자르고 붙이면 -> stack 써야 시간 초과 안남
# 괄호 짝짓기 문제?
# stack에 넣은 다음 문자가 같아야 빠지게?

def solution(s):  # 문자열
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return 0
    else:
        return 1

# <피드백>
# 괄호 문제와 유사
# 짝 짓는다하면 -> stack
# slice 로 풀면 시간초과