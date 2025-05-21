# Q. 프로세스
#
# 문제 설명
# 운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.
#
# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.
#
# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# priorities의 길이는 1 이상 100 이하입니다.
# priorities의 원소는 1 이상 9 이하의 정수입니다.
# priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
# location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
# priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.
# 입출력 예
# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
# 입출력 예 설명
# 예제 #1
#
# 문제에 나온 예와 같습니다.
#
# 예제 #2
#
# 6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가 [1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다. 따라서 A는 5번째로 실행됩니다.


# 특정 프로세스가 몇번째로 실행되는지 알아내야 한다

# 1. 실행 대기 큐(Queue) 에서 대기중인 프로세스 하나 꺼냄
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있으면 방금 꺼낸 프로세스를 다시 큐에 넣음
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행
# 3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료

# ex. [2, 1, 3, 2] 의 우선순위라면
# -> [C, D, A, B] 순으로 실행
# 우선순위 : priorities
# 몇 번째로 실행되는지 알고싶은지 프로세스의 위치 : location

# <풀이>
# 우선순위가 같은데 들어올 수 있다
# 선입선출 된다, 높은게 존재하면 다시 들어간다

# 1. 실행 대기 큐에서 하나 꺼내서
# 2. 나머지 애들과 비교해서 더 높은 프로세스 있으면 다시 큐에 넣고
# 3. 없으면 방금 꺼낸 것 실행 -> 별도의 완료 list에 넣기

from collections import deque


def solution(priorities, location):
    completed_arr = []
    wait_queue = deque(priorities)
    wait_process = deque()
    for i in range(len(priorities)):
        wait_process.append(i)

    while wait_queue:
        current_process = wait_queue.popleft()
        current_process_count = wait_process.popleft()
        for process in wait_queue:
            if current_process < process:
                wait_queue.append(current_process)
                wait_process.append(current_process_count)
                break
        else:
            completed_arr.append(current_process_count)

    return completed_arr.index(location) + 1

# <피드백>
# 각 작업의 이름의 배열은 따로 존재하지 않으므로 직접 지정해줘야 한다
# 나는 두개의 deque를 만들었으나, 더 좋은 방법으로는
# 아예 deque 에 넣는 형식을 index를 포함하도록 하는 것이다
# 아래 enumerate(arr) 로 index를 넣을 수 있다
# 이 index 를 location 과 비교할 수 있게 된다

# * (element, index) for index, element in enumerate(arr) 로 index를 포함해서 꺼낼 수 있다
# * if any(q 관련 조건문 for q in queue) 를 통해 하나라도 맞는지 여부 판단이 가능하다


from collections import deque

def solution1(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    order = 0

    while queue:
        current = queue.popleft()
        # 하나라도 현재보다 우선순위 높은 게 있으면 다시 뒤로
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else: # 이 작업이 가장 우선 순위가 높으므로 위치 변동이 없으니
            order += 1 # 몇 번째인지 관리
            if current[1] == location: # 구하고자 하는 위치라면 바로 return
                return order