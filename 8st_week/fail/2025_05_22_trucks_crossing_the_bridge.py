# Q. 다리를 지나는 트럭
# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
#
# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
#
# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	[]	[]	[7,4,5,6]
# 1~2	[]	[7]	[4,5,6]
# 3	[7]	[4]	[5,6]
# 4	[7]	[4,5]	[6]
# 5	[7,4]	[5]	[6]
# 6~7	[7,4,5]	[6]	[]
# 8	[7,4,5,6]	[]	[]
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.
#
# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
#
# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.
# 입출력 예
# bridge_length	weight	truck_weights	return
# 2	10	[7,4,5,6]	8
# 100	100	[10]	101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110

# <문제분석>
# 정해진 순서로 건너야 한다
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 한다
# 다리에는 트럭이 최대 bridge_length 대 올라갈 수 있고
# 다리는 weight 이하까지의 무게를 견딜 수 있다
# * 단 다리에 완전히 오르지 않은 트럭의 무게는 무시

# ex.
# 트럭 2대 까지 + 무게 10kg 까지 조건 하
# 무게 [7, 4, 5, 6] 이 순서대로 최단 시간에 건너려면

# 경과 시간 / 다리를 지난 트럭 / 다리를 건너는 트럭 / 대기 트럭
# 0초일 때는 대기
# 1초가 됐을 때 7 kg 한 대
# 2초가 됐을 때 7 건너가고
# 3초 됐을 때 7끝나고, 4 올라가고
# 4초 됐을 때 5 올라가고
# 5초 됐을 때 4 끝
# 6초 됐을 때 5 끝, 6 올라가고
# 7초 됐을 때 6 건너고 있고
# 8초 됐을 때 6도 끝
# -> 즉 7입장에서 1초 대 올라가고 2초 대 건너고 3초 대 끝난다

# <풀이>
# 동작) 올라가고, 건너고, 끝나고 = 3초 걸림
# -> 각 트럭마다 걸린 시간을 별도로 관리 필요
# 모든 트럭이 다 건너갈 때 까지 = bridge_length가 빌 때 까지
# 다리를 지난 트럭
# 선입선출

from collections import deque
# def solution(bridge_length, weight, truck_weights):  # 한 번에 최대 개수, 최대 무게, 트럭마다 무게
#     answer = 0
#
#     wait_truck_queue = deque(truck_weights)  # 대기중인 트럭
#     ongoing_truck_queue = deque()  # 건너는중인 트럭 + 소요 시간
#     completed_truck_queue = deque()  # 끝난 트럭
#
#     while wait_truck_queue:
#         answer += 1  # 소요 시간
#         # 최대 개수와 최대 무게 제한에 안걸리면 건너게 함
#         if len(ongoing_truck_queue) < bridge_length and sum(ongoing_truck[0] for ongoing_truck in ongoing_truck_queue) + \
#                 wait_truck_queue[0] <= weight:
#             ongoing_truck_queue.append([wait_truck_queue.popleft(), 1])
#         # ongoing 에서 3초 채운 애들 빼내기 아니면 1초 더해주기
#         new_ongoing_truck_queue = deque()
#         for ongoing_truck in ongoing_truck_queue:
#             if ongoing_truck[1] < 3:
#                 new_ongoing_truck_queue.append([ongoing_truck[0], ongoing_truck[1] + 1])
#         ongoing_truck_queue = new_ongoing_truck_queue
#
#     return answer

# <피드백>
# 문제 이해를 잘못했다.
# '다리에는 트럭이 최대 bridge_length대 올라갈 수 있으면'
# 라고 나와서 진짜 다리 위에 트럭의 개수를 제한하는 걸로 생각했는데
# 입출력 예제를 보면 다리를 건너는데 소요 시간을 의미하는 거였다

def solution(bridge_length, weight, truck_weights):
    from collections import deque

    wait_truck_queue = deque(truck_weights)
    bridge_queue = deque()  # (트럭 무게, 다리 위 경과 시간)
    time = 0
    current_weight = 0

    while wait_truck_queue or bridge_queue:
        time += 1

        # 1. 먼저 다리 위 트럭 시간 증가
        bridge_queue = deque([(w, t + 1) for w, t in bridge_queue])

        # 2. 다리 위 가장 오래된 트럭이 다리를 완전히 건넜으면 제거
        if bridge_queue and bridge_queue[0][1] > bridge_length:
            truck_weight, _ = bridge_queue.popleft()
            current_weight -= truck_weight

        # 3. 대기 트럭 중 다리에 올릴 수 있으면 올림
        if wait_truck_queue and current_weight + wait_truck_queue[0] <= weight and len(bridge_queue) < bridge_length:
            truck_weight = wait_truck_queue.popleft()
            bridge_queue.append((truck_weight, 1))  # 올린 순간 1초 경과로 시작
            current_weight += truck_weight

    return time