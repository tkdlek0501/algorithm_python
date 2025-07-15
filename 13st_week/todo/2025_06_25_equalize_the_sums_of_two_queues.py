# Q. 두 큐 합 같게 만들기

# <문제분석>
# 길이가 같은 두 개의 큐(선입선출)
# 하나의 큐를 골라 원소 pop 하고
# 다른 큐에 넣는 작업을 통해 원소의 합이 같도록 만들려고 한다
# 이 때 필요한 작업의 최소 횟수를 구하려고 한다 -> bfs?
# 한 번의 pop과 한번의 insert를 합쳐서 1회 수행한 것으로 간주

# 큐를 배열로 표현했다
# queue1 과 queue2 의 길이 300,000
# -> bfs를 쓰기에는 횟수가 너무 많아진다
# 동작은 2가지 가능
# queue1 -> queue2
# queue2 -> queue1
# 큰 쪽에서 작은 쪽으로 넘겨주며 맞춰줘야 한다

from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    total = sum(q1) + sum(q2)
    if total % 2 != 0:
        return -1  # 합이 홀수면 절대 같게 못함
    target = total // 2

    max_len = len(q1) + len(q2)
    cnt = 0
    sum1 = sum(q1)

    # 투포인터처럼 진행
    while cnt <= max_len * 3:  # max_len * 2 정도면 충분히 모든 조합을 시도할 수 있으나 여유롭게 3배수
        if sum1 == target:
            return cnt
        elif sum1 > target:  # 1이 크면
            val = q1.popleft()  # 1에서
            sum1 -= val
            q2.append(val)  # 2로 이동
        else:  # 1이 작으면
            val = q2.popleft()  # 2에서
            sum1 += val
            q1.append(val)  # 1로 이동
        cnt += 1

    return -1

# <피드백>
# while 문 설정이 중요한 문제 length의 *3 이 적절한 범위
# sum() 은 while 내에서 하면 위험하므로 +-로 계산
# 로직은 쉬우나 범위 설정이 감이 안오는 케이스