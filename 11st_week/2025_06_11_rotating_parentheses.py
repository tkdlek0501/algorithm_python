# Q. 괄호 회전하기

# <문제분석>
# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의
# 괄호 -> stack?
# (), [], {}
# 만약 A가 올바른 괄호 문자열이라면 (A), [A], {A} 도 올바른 괄호 문자열
# A, B가 올바른 괄호 문자열이라면 AB도 올바른 괄호 문자열

# 대, 중, 소괄호로 이루어진 문자열 s 주어지면
# s를 왼쪽으로 x칸 만큼 회전시켰을 때 (최소 0부터 최대는 s의 길이)
# s가 올바른 괄호 문자열이 되게하는 x의 개수 구하기
# s의 길이는 1,000 이하

# 회전?
# [](){} 을 왼쪽으로 1칸 회전 -> 맨앞이 맨뒤로 오게됨 ](){}[


def solution(s):
    answer = 0

    for i in range(len(s)):  # 회전 하면서
        changed_s = s[i:] + s[:i]  # 변한 문자열
        stack = []
        is_break = False
        for c in changed_s:
            if c == '(':
                stack.append('(')
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    is_break = True
                    break
            if c == '{':
                stack.append('{')
            if c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    is_break = True
                    break
            if c == '[':
                stack.append('[')
            if c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    is_break = True
                    break

        if len(stack) == 0 and not is_break:  # 올바른 문자열이고 break 케이스 아니라면
            answer += 1

    return answer

# <피드백>
# 리팩토링 하자면
def solution1(s):
    answer = 0
    brackets = {')': '(', '}': '{', ']': '['}

    for i in range(len(s)):
        changed_s = s[i:] + s[:i]
        stack = []
        for c in changed_s:
            if c in brackets.values():  # 여는 괄호
                stack.append(c)
            elif c in brackets:  # 닫는 괄호
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1

    return answer