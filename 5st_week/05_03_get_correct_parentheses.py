# 문제 설명
# 카카오에 신입 개발자로 입사한 콘은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무 과제를 받았습니다.
# 소스를 컴파일하여 로그를 보니 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 되었습니다.
# 수정해야 할 소스 파일이 너무 많아서 고민하던 콘은 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.
#
# 용어의 정의
# '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다.
# 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.
# 예를 들어, "(()))("와 같은 문자열은 균형잡힌 괄호 문자열 이지만 올바른 괄호 문자열은 아닙니다.
# 반면에 "(())()"와 같은 문자열은 균형잡힌 괄호 문자열 이면서 동시에 올바른 괄호 문자열 입니다.
#
# '(' 와 ')' 로만 이루어진 문자열 w가 균형잡힌 괄호 문자열 이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다.
#
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.
#
# 균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 올바른 괄호 문자열로 변환한 결과를 반환하시오.

# <문제분석>
# 용어 - 균형잡힌 괄호 문자열 = ( 와 ) 의 개수가 같으면
# 용어 - 올바른 괄호 문자열 = ( 와 ) 의 짝도 모두 맞을 경우
# 문자열 w 가 균형잡힌 문자열이라면 위 알고리즘을 통해 올바른 괄호 문자열로 변환 가능
# 균형잡힌 괄호 문자열 p 가 매개변수로 주어지면 올바른 괄호 문자열로 변환한 결과를 반환

# <문제풀이>
# 1. 먼저 주어진 문자열이 비어져 있는지 확인 후 비어져 있으면 빈 문자열을 반환
# 2. 주어진 문자열에 대해서 두 개의 균형잡힌 괄호 문자열 u, v 로 분리, 단 u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 하며, v는 빈 문자열일 수 있다
# => u는 더 이상 분리할 수 없는 최소 단위가 돼야 한다
# 3. 위 문자열 u에 대해서 문자열 v에 대해 1단계 부터 다시 수행
# 3-1. 수행한 결과를 u에 이어 붙인 후 반환
# 4. 문자열 u가 올바른 괄호 문자열이 아니라면 올바른 괄호 문자열이 되기 위해서
# 4-1 부터 4-5 수행

# <코드변환>
# 1. if(len(주어진 문자열)) == 0 이면 바로 반환
# 2. 주어진 문자열을 두 개의 균형잡힌 괄호 문자열 u, v로 분리, 개수가 동일하면 균형잡힌 괄호 문자열 이므로 이를 어떻게 나눌 수 있는지 생각
# 3. v에 대해서도 1단계 부터 수행

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string): # 이미 올바른 괄호라면 바로 반환
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)

def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if not stack: # 예외 케이스: 없는 데 pop 하려고 하면 그건 False
                return False
            stack.pop()

    return len(stack) == 0

from collections import deque

balanced_parentheses_string = "()))((()"

def change_to_correct_parenthesis(balanced_parentheses_string):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if balanced_parentheses_string == '':
        return balanced_parentheses_string
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = separate_to_u_v(balanced_parentheses_string)
    # print("u : ", u, "v : ", v)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v) # v에 대해 1단계 부터 재귀적으로 수행하고 u 에 이어 붙어 반환
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #     #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #     #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #   4-3. ')'를 다시 붙입니다.
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    #   4-5. 생성된 문자열을 반환합니다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])

# 2.
def separate_to_u_v(string):
    queue = deque(string)
    left_parenthtis_count, right_parenthtis_count = 0, 0 # 왼쪽, 오른쪽 괄호 개수
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left_parenthtis_count += 1
        if char == ')':
            right_parenthtis_count += 1

        if left_parenthtis_count == right_parenthtis_count: # 개수가 최초로 동일한 상태가 되면 u는 더 이상 분리할 수 없는 균형잡힌 문자열이 됨
            break
    # v는 queue에 남아있는 문자열 넣어주면 됨
    v = ''.join(queue) # 파이썬에서 join 은 특정 리스트 입력시 원소들을 합쳐서 문자열로 만들어 주는 함수

    return u, v

# 4-4.
def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ")"
        elif char == ")":
            reversed_string += "("
    return reversed_string

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))