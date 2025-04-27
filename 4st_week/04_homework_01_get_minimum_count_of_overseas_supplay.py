# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다.
# 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies), 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때,
# 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.
# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.

import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# tip
# heap = []
# heapq.heappush(heap, 4)
# heapq.heappop(heap)

# 문제 분석
# 하루에 밀가루 1톤씩 사용
# k일 이후에 밀가루 공급이 가능해야 돼서 해외에서 수입해야 한다
# 현재 공장에 남아있는 밀가루 수량 : stock
# 밀가루 공급 일정 : dates / 해당 시점에 공급 가능한 밀가루 수량 : supplies
# 원래 공장으로부터 공급 받을 수 있는 시점 : k
# 밀가루가 떨어지지 않고 운영하려면 최소 몇 번 해외 공장으로 부터 공급 받아야 하는지 구해야 한다
# dates[i] 에는 i번째 공급 가능일이 들어있고, supplies[i] 에는 그 날짜에 공급 가능한 밀가루 수량이 들어있다

# 아이디어
# 하루에 밀가루 1 씩 소비
# k일 까지 버텨야 함
# 최소한의 공급 횟수로 밀가루가 떨어지지 않게 해야함
# -> 공급을 한 번 할 때 어떤 날짜든 가능한 범위 내에서 한 번에 최대한 많이 가져와야 한다
# 지속적으로 리소스를 소모하면서, 필요할 때 공급해야 하는데, 그 공급 횟수를 최소화 해야하는 문제 패턴
# 매 순간 최적의 선택을 반복 -> 그리디
# 여러 선택지 중 가장 큰 값을 뽑아야 한다 -> 우선순위 큐 (힙)

# 문제 풀이
# 재고가 바닥 나기 전에 가장 많은 공급향을 최소한의 횟수로 가져오는 게 목적이다
# 1. 현재 재고 상태에 따라 최대값을 가져와야 한다 (동적인 상황 -> 정렬을 쓸 수 없다)
# 2. 제일 많은 값만 가져오면 된다
# -> maxHeap

# 재고가 바닥 나면 안된다 -> stock > k 를 계속 유지해야 한다
# heap 에다가 넣어둔 다음에 최고로 많은 재고들을 꺼내서 stock에 넣어준다
# 그 전에 현재 재고가 바닥나는 시점 이전에 공급해야 한다!
# -> 현재 stock이 dates 보다 높아야 한다
def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0 # 공급 받는 횟수
    last_added_date_index = 0 # 마지막 공급 일자의 인덱스
    max_heap = []
    while stock <= k: # stock 이 k보다 크면 멈춘다 (마지막 일까지 버틸 공급향이 충분할 때까지)

        # 현재 stock일 이전까지 공급 가능한 모든 공급을 max_heap에 추가 (높은 일자는 도달하기 전에 재고 바닥 나므로 검사하는 의미가 없다)
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, supplies[last_added_date_index] * -1) # min_heap을 max_heap 처럼 쓰기 위해 * -1 처리
            last_added_date_index += 1

        supply = heapq.heappop(max_heap) * -1
        stock += supply
        answer += 1

    return answer

# 공급 받을 수 있는 것들 중 가장 큰 값을 stock 에 넣어줌으로써 결국 k보다 크게 만드는 게 목표
# k 에 도달하기 전에도 재고가 바닥 날 수 있으므로 stock 보다 높은 일자의 값은 두 번째 while 문에서 빼준다

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))