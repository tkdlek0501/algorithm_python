# Q.초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 함수를 완성하세요.
#
# prices = [1, 2, 3, 2, 3]
# answer = [4, 3, 1, 1, 0]

# 예를 들어서 0번째 인덱스인 1의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#    -> -> -> ->
# [1, 2, 3, 2, 3] (전부 안떨어졌으니까 4초!)
#
# 1번째 인덱스인 2의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#       -> -> ->
# [1, 2, 3, 2, 3] (전부 안떨어졌으니까 3초!)
#
# 2번째 인덱스인 3의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#          ->
# [1, 2, 3, 2, 3] (1초 뒤에 떨어졌으니까 1초)
#
# 3번째 인덱스인 2의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#             ->
# [1, 2, 3, 2, 3] (전부 안떨어졌으니까 1초)
#
# 4번째 인덱스인 3의 경우에는 마지막이라서 0초간 안 떨어집니다.
# [1, 2, 3, 2, 3]

# 아이디어
# 맨 앞부터 시작해서 나머지 값과 하나씩 비교하며 나머지 값이 크거나 같으면 횟수를 +1 로 계산하는 작업
# 새로운 배열에 횟수를 넣어야 된다
# 자료구조) 맨 앞부터 시작하니까 맨 앞부터 빼낼 수 있게 queue 사용하면 좋겠다
# 함정이 있다.. 3, 2, 3 의 경우 3 기준으로 0초가 아니라 1초 유지로 본다 1초 뒤 떨어졌으니까

prices = [1, 2, 3, 2, 3]

from collections import deque
def get_price_not_fall_periods(prices):
    result = [] # stack 처럼 쓰기
    prices_queue = deque(prices) # collections.deque 를 이용해서 queue 자료구조 사용

    while prices_queue: # prices_queue 가 비어있지 않다면 계속 반복
        price_not_fall_period = 0
        current_price = prices_queue.popleft()
        for next_price in prices_queue:
            if current_price <= next_price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period)
    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))