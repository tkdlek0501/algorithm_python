# Q. 타겟 넘버
#
# 문제 설명
# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2
# 입출력 예 설명
# 입출력 예 #1
#
# 문제 예시와 같습니다.
#
# 입출력 예 #2
#
# +4+1-2+1 = 4
# +4-1+2-1 = 4
# 총 2가지 방법이 있으므로, 2를 return 합니다.



# <문제분석>
# n개의 음이 아닌 정수들
# 이 정수들을 순서를 바꾸지 않고
# 적절히 더하거나 빼서 타겟 넘버를 만들어야 한다
# 맨 앞의 숫자에도 (-) 붙일 수 있다

# 입력) 사용할 수 있는 숫자가 담긴 배열 numbers
# / 타겟넘버 target

# 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return

# <풀이>
# 모든 경우의 수를 생각해야 한다
# -를 붙일 수 있고 +를 붙일 수 있다
# 재귀를 통해 -, + 를 해준다?
# 그 결과 값이랑 target 비교해서 count 한다

# 하나는 +, 하나는 - 해주는 함수 만들어서 재귀 대신 -> stack 이용

def solution(numbers, target):
    stack = [(0, 0)]
    count = 0

    while stack:
        current_sum, idx = stack.pop()
        if idx == len(numbers):
            if current_sum == target:
                count += 1
        else:
            stack.append((current_sum + numbers[idx], idx + 1))
            stack.append((current_sum - numbers[idx], idx + 1))

    return count

# <피드백>
# 모든 경우의 수를 탐색하는 DFS, BFS 문제에서는 재귀보다 stack 을 이용하여 푸는 게 좋다
# stack에 다음에 가능한 경우를 계속 넣어주면 답 찾을 수 있다

from collections import deque
def solution1(numbers, target):  # 사용할 수 있는 숫자 배열, 타겟 넘버
    answer = 0

    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))
    while queue:
        num, idx = queue.popleft()
        if idx == len(numbers) - 1:
            if num == target:
                answer += 1
        else:
            queue.append((num + numbers[idx + 1], idx + 1))
            queue.append((num - numbers[idx + 1], idx + 1))

    return answer

# <피드백>
# queue 로 풀어도 괜찮으나 초기값을 초기화 할 때
# queue.append((0, 0)) 으로 시작하는 게 더 좋다

