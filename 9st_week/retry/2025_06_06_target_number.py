# <문제분석>
# n개의 음의 아닌 정수들
# 순서 바꾸지 않고 더하거나 빼서 타겟넘버 만들기
# 맨 앞 숫자도 부호 가질 수 있음
# 방법의 수 return

# <풀이>
# 첫 번 째 숫자부터 2가지 경우의 수를 가짐
# 숫자를 하나씩 꺼내면서
# for 문 돌면서 합을 합산

def solution(numbers, target):  # 정수 배열 [1, 1, 1, 1, 1], 타겟넘버 3
    count = 0

    stack = [(0, 0)]  # idx, sum
    while stack:
        idx, sum_value = stack.pop()

        if idx == len(numbers):
            if sum_value == target:
                count += 1
        else:
            stack.append((idx + 1, sum_value + numbers[idx]))
            stack.append((idx + 1, sum_value - numbers[idx]))

    return count






