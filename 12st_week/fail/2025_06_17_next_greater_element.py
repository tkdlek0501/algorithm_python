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

# <피드백>
# 문제 접근 자체는 괜찮았다
# for문을 돌며 slice 하는 직관적인 풀이는 범위에 의해 할 수 없다 (시간복잡도 = O(N^2))
# 그렇다고 BFS를 도입하기에 적절하지 않고
# 이분탐색을 하기에도 정렬을 시켜서 풀 수 없다

# 범위가 커서 탐색이 어려운 상황에서는 또다른 자료구조를 써서 그 안에서 해결하는 방법을 써야 한다
# 맨 앞부터 생각하면 범위가 넓지만 맨 뒤부터 생각하면 좁은 범위 내에서 풀 수 있다
# 맨 뒤 부터 생각하므로 stack 을 떠올릴 수 있다

# 이 문제의 핵심은 '뒤에서 부터 풀자'(stack 쓰자)
# stack에서 자기보다 작거나 같은 값은 불필요해진다는 아이디어

# 정방향 풀이도 가능하다 (인덱스로 생각)
# 현재 인덱스의 값을 모르니 stack에 넣고 다음 값과 비교해서 그 인덱스들의 뒷 큰 수를 찾아주기
def solution1(numbers):
    stack = [] # 아직 값을 찾지 못한 인덱스
    result = [-1] * len(numbers)

    for i in range(len(numbers)): # 인덱스 돌면서
        while stack and numbers[stack[-1]] < numbers[i]: # 스택에 남아있는 인덱스에 해당하는 수가 현재 값보다 작다면
            result[stack.pop()] = numbers[i] # result 에 그 인덱스(뒷 큰 수 넣을 자리)에 현재값을 넣어준다

        stack.append(i) # 현재 인덱스 넣어주기

    return result
