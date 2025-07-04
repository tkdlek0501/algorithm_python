# Q. 롤케이크 자르기

# <문제분석>
# 롤케이크를 두 조각으로 잘라서
# 롤케이크에는 여러 토핑들이 일렬로 올려져 있다
# 공평하게 나눠 먹으려고 하는데
# 크기보다 토핑의 종류에 더 관심
# 크기나 토핑의 개수에 상관없이 각 조각에 동일한 가짓수의 토핑이 올라가야 한다

# ex.
# 롤케이크에 4가지 종류의 토핑이 올라가 있다
# [1, 2, 1, 3, 1, 4, 1, 2] 순서로
# 만약 세 번째 토핑(1) 네번째 토핑(3) 사이를 자르면
# [1, 2, 1] , [3, 1, 4, 1, 2] -> 공평하지 않다
# [1,2,1,3] , [1,4,1,2] -> 가짓수 3개씩 공평하다
# 공평하게 자르는 방법은 여러가지일 수 있다
# 어떤 경우는 공평하게 나누지 못할 수도 있다

# 토핑들의 번호를 저장한 정수 배열 topping 이 매개변수로 주어진다면
# 롤케이크를 공평하게 자르는 방법의 수를 return 하도록 해야한다
# topping 의 길이 1,000,000

# <풀이>
# 1. 2개의 배열로 부터 각 set 를 만든다
# -> 이때 for 문 안에서 slicing 쓰면 시간복잡도 N^2 되므로 못씀
# -> slicing 없이 left와 right 로 만드려면 right(Counter를 통해 만든)에 다 몰아넣고 left는 진행하면서 add하고 right는 제거하는 방식으로
# set의 길이를 비교한다
# 같으면 방법의 수를 +1 한다

from collections import Counter


def solution(topping):
    answer = 0
    right = Counter(topping)
    left = set()

    for i in range(len(topping)):
        t = topping[i]  # i번째 토핑을
        left.add(t)  # left 에 더하고
        right[t] -= 1  # right 에서는 빼주고
        if right[t] == 0:  # right에서 0개가 된다면
            del right[t]  # 해당 토핑 제거

        if len(left) == len(right):
            answer += 1

    return answer

# <피드백>
# 범위가 1번의 순회만 가능한 정도이므로
# left, right 를 나눠서 생각해야 한다
# 한 쪽에서 다른 한쪽으로 넘겨주는 아이디어로 가야한다

# Couter를 써야 right 의 수를 대폭 줄일 수 있다
# right를 단순히 stack이나 queue로 만들어봤자 set을 써야 하는데 그러면 O(N^2) 된다
# 거기다 순서가 중요한게 아니라 전체 기준으로 가짓수만 가지고 판별하기 때문에
# 이런 문제에서 dict 까지 고려하는 사고를 가져야 한다

# del right[t] 로 키를 삭제할 수 있다