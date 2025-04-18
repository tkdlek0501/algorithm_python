# Q. 올바른 괄호
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다.
# 예를 들어
#
# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.
#
# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 True 를 반환하고
# 아니라면 False 를 반환하시오.

# 문제분석
# 1. 괄호가 올바르게 짝지었다 = ( 로 열려있으면 반드시 짝지어서 ) 로 닫혀야 한다
# 2. ()() (())() 는 되는데 )()( 등은 안된다
# 3. 짝이 맞으면 True 반환 아니면 False 반환

# 아이디어
# 1. 단순히 개수로 비교하면 안 된다
# 2. 열린게 먼저 있어야 한다
# 3. 케이스 정리
# ( 로 열려 있을 때 ((((())))) ()(()))
# 보통 괄호가 닫혀 있는 것을 확인 하려면 가장 안 쪽 부터 찾아서 닫혔는지 보니까 이 방법을 쓴다
# -> 순서대로 데이터를 쌓아놓고 가장 마지막에 있는 데이터를 꺼낼 수 있는 stack 이 적합하다!
# (()) 은 True
# ) 는 여는 괄호가 안 찾아지니 False
# ((()))) 여는 괄호의 개수와 닫는 괄호의 개수가 안맞으니 False -> 일단 여는 괄호의 개수와 닫는 괄호의 개수도 맞긴 해야 한다
# ())() -> 얘도 개수 안 맞음
# ((()) -> 얘도

# 풀이방법
# stack 이용해서 ( 로 쌓아두고 )로 제거한 후 남은 게 없다면 True 이고 남아 있는게 있다면 False

def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append("(")
        else:
            if not stack: # 예외 케이스: 없는 데 pop 하려고 하면 그건 False
                return False
            stack.pop()

    return len(stack) == 0

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))