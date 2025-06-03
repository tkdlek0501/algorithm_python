# Q. 프로세스

# <문제분석>
# 규칙에 따라 프로세스 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내야 한다

# 1. 실행 대기 큐(Queue) 에서 대기중인 프로세스 하나를 꺼내고
# 2. 대기중인 프로세스 중 우선순위가 더 높은 프로세스 있으면 방금 꺼낸 것은 다시 큐에 넣기
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스 실행
# 3-1. 한 번 실행한 프로세스는 다시 큐에 넣지 않음

# ex.
# [A, B, C, D] 대기 큐
# [2, 1, 3, 2] 우선 순위
# -> [C, D, A, B] 실행

from collections import deque


def solution(priorities, location):  # 중요도 배열, 몇 번째로 실행되는지 알고 싶은 프로세스 위치(인덱스)

    wait_queue = deque()  # [(인덱스, 중요도)]
    for i in range(len(priorities)):
        wait_queue.append((i, priorities[i]))
    # print(wait_queue)

    completed_arr = []  # 완료된 것 부터 넣어지는 배열

    while wait_queue:
        q = wait_queue.popleft()

        for idx, p in wait_queue:
            if p > q[1]:  # 중요도 더 큰 게 있으면
                wait_queue.append(q)
                break
        else:  # 없으면 꺼내기
            completed_arr.append(q[0])

    # print(completed_arr)

    return completed_arr.index(location) + 1