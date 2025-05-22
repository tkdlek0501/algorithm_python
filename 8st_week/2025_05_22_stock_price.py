# Q. 주식가격
# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

# <문제분석>
# 초 단위 주식가격 prices
# 가격이 떨어지지 않은 기간은 몇 초인지를 return

# ex.
# prices [1,2,3,2,3]
# 1초 시점의 1은 끝까지 떨어지지 않았고 -> 4
# 2초 시점의 2도 끝까지 떨어지지 않았고 -> 3
# 3초 시점의 3은 1초 뒤에 가격 떨어짐 -> 1
# 4초 시점의 2는 가격 안떨어짐 -> 1
# 5초 시점은 마지막이라 -> 0

# <풀이>
# prices 를 deque 로 만들어 하나씩 뽑으며 보자

from collections import deque
def solution(prices):
    answer = []

    prices_queue = deque(prices)
    while prices_queue:
        current_price = prices_queue.popleft()
        time = 0

        if len(prices_queue) == 0:
            answer.append(0)
        else:
            for other_price in prices_queue:
                time += 1
                if other_price < current_price:
                    answer.append(time)
                    break
            else:
                answer.append(time)

    return answer

# <피드백>
# 아래와 같이 queue 를 쓰지 않고 풀 수 있다

def solution1(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
