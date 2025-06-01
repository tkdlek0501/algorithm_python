# <문제분석>

# 일차선 다리 정해진 순으로 건너야 함
# 모든 트럭이 다리를 건너려면 걸리는 시간 최소 몇 초인지
# 최대 bridge_length 대 올라갈 수 있고
# 다리는 weigth 이하까지의 무게를 견딜 수 있다
# *단 다리에 완전히 오르지 않은 트럭의 무게는 무시

# ex.
# 제한) 트럭 2대 + 무게 10
# 무게 [7, 4, 5, 6] 이 순서대로?
# 1초 -> 7 건너는 중 4, 5, 6 기다림
# 2초 -> 7 건너는 중
# 3초에 7 끝나고 4, 5 건널 수 있음

# 선입선출이므로 queue
# 제한에 따라 꺼내줘야 한다
# 건너는 시간 주의

# <풀이>
# 다리를 지난 트럭은 따로 관리 안해도 되고
# 다리를 건너는 트럭은 자기 무게, 소요 시간 관리하고 있어야 함
# while 문은 대기 트럭이 모두 없어질 때 까지

from collections import deque


def solution(bridge_length, weight, truck_weights):
    wait_truck_queue = deque(truck_weights)  # 대기 트럭
    cross_truck_queue = deque()  # 다리를 건너는 트럭, 무게/ 경과시간
    cross_weight = 0  # 다리 위 무게
    time = 0  # 전체 소요 시간
    while wait_truck_queue or cross_truck_queue:
        time += 1  # 시간 증가

        # 다리 위 트럭들 경과 시간 증가
        cross_truck_queue = deque([(w, t + 1) for w, t in cross_truck_queue])

        # 경과 시간 지난 트럭 빼주기
        if cross_truck_queue and cross_truck_queue[0][1] > bridge_length:
            w, t = cross_truck_queue.popleft()
            cross_weight -= w

            # 대기 트럭 넣어주기 (무게, 대수)
        if wait_truck_queue and weight >= cross_weight + wait_truck_queue[0] and bridge_length > len(cross_truck_queue):
            wait_truck = wait_truck_queue.popleft()
            cross_truck_queue.append((wait_truck, 1))
            cross_weight += wait_truck

    return time