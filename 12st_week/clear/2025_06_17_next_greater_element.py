# Q. 뒤에 있는 큰 수 찾기

# <문제분석>
# 정수 배열 numbers
# 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서
# 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수 라고 한다
# numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례대로 담은 배열을
# return 하도록 해야 한다
# 단, 뒷 큰수가 존재하지 않으면 -1을 담는다
# numbers <= 1,000,000
# -> for 문 돌아서 slice 할 수 없다

# <풀이>
# 자신보다 크면서 가장 가까이 있는 수 찾기
# ex.
# [2, 3, 3, 5] -> [3, 5, 5, -1]
# 자기 자신과 비교하면서 큰 값을 찾아야 하는데 최악의 경우 모든 원소를 다 찾아봐야 한다
# 이분탐색? -> 정렬 해야돼서 안됨
# BFS는 가능한가? 최단으로 찾아야 하니까 -> 그래도 안될 것 같다. visit을 쓸만한 곳이 없다

# 2는 다음에 있는 3
# 3은 그다음 2번째에 있는 5
# 5는 -1
# 뒤에서 부터 탐색하면 되나?
# 맨 뒤는 -1
# 그 다음은? 맨 뒤 넣고 찾기

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1): # 뒤 부터 돌기
        # stack에서 자기보다 작거나 같은 건 제거 - 현재값보다 작거나 같으면 앞의 수에서는 쓸모가 없어지기 때문
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        # 스택이 비어있지 않으면 top이 뒷 큰수
        if stack:
            answer[i] = stack[-1]
        # 현재 숫자 push
        stack.append(numbers[i])

    return answer

def solution1(numbers):
    answer = [-1] * len(numbers)  # numbers의 개수만큼 뒷큰수 배열

    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:  # 큰 수 발견 시
            answer[stack.pop()] = numbers[i]
        stack.append(i)  # i 인덱스 담기

    return answer

# <피드백>
# 10 분 이내로 풀이 가능
# i번째 요소의 뒷 큰수를 찾기 위해서
# i 인덱스를 stack에 넣어두고 순회하며 큰 수 찾았을 때 마다 처리해주면 된다