# Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.
#
# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
#
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다



# <문제 분석>
# 코니와 브라운 2 사람이 존재
# 게임이 끝나는데 걸리는 '최소 시간'을 구해야 한다
# *끝나는 조건 : 브라운이 코니를 잡거나 코니가 너무 멀리 달아나면 끝난다
# 브라운 -> 코니 따라간다

# 코니)
# 처음 위치 C에서 1초 후 1만큼 움직이고
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1 만큼 움직인다
# 즉 C, C + '1', C + 3(1 + '2'), C + 6(3 + '3')...
# => *+1 등차수열로 가속 = 현재 경과 시간 만큼 증가

# 브라운)
# 현재 위치 B에서 다음 순간
# B - 1 or
# B + 1 or
# 2 * B
# 중 하나로 움직일 수 있다
# => *모든 경우의 수 다 봐야한다 DFS or BFS

# 코니와 브라운 모두 위치 p는 조건 0 <= x <= 200,000 을 만족
# 브라운은 범위를 벗어나는 위치로는 이동 못하고, 코니가 범위를 벗어나면 게임이 끝난다

# 다시,
# 게임이 끝나는 데 걸리는 최소 시간은
# 1. 브라운이 코니를 따라 잡거나 B >= C
# 2. 코니가 범위를 벗어나면 -> C > 200,000
# 그 때 걸리는 시간 중 작은 값이다

# <문제 풀이>
# 1초마다 코니와 브라운이 현재 위치 각각 C, B에서 움직인다
# 코니는 +1 씩 매초마다 등차수열로 이동
# => *규칙적이므로 배열
# 브라운은 B - 1 or B + 1 or 2 * B 로 이동
# => *불규칙적이므로 딕셔너리
# => *+ 모든 경우의 수를 다 나열할 필요가 있으므로 BFS 를 사용해야겠다
# while 문 조건은 코니 즉 C의 범위가 200,000 을 벗어나는 때로 하고
# 또 다른 종료 조건은 브라운이 코니를 따라 잡았을 때로 한다

# 브라운이 관건인데
# 초 마다 위치할 수 있었던 곳들이 여러개 이므로
# 배열 안에 딕셔너리로 관리하자
# => [{}, {}, {}, ...]


from collections import deque

c = 11 # 코니 초기 위치
b = 2 # 브라운 초기 위치
# 브라운이 코니 잡는다 or 코니가 범위 벗어나면 끝
# 브라운이 코니를 잡는 다는 것은 같은 시간에 같은 위치가 돼야 한다는 것


def catch_me(cony_loc, brown_loc):
    time = 0 # 시간
    queue = deque() # 브라운의 현재 위치, 시간 저장할 용도; 시간과 위치 모두 비교 대상이므로
    queue.append((brown_loc, 0))

    # 시간으로 매 순간을 비교하는 게 일반적인 상식이지만
    # 이 문제에서는 시간이 아닌 범위 조건이 주어졌으므로 이를 기준 while 돌면서 풀어야 한다!
    visited = [{} for _ in range(200001)] # [{}, {}, ...], 브라운의 모든 방문 정보

    while cony_loc <= 200000: # 코니의 범위 제한
        cony_loc += time # 시간마다 +1 등차수열 이므로 현재 경과 시간을 더해준다
        if time in visited[cony_loc]: # 코니 위치와 동일한 위치 값이 있는 브라운의 데이터 중 같은 시간의 데이터가 있는지
            return time # 시간과 위치가 동일한 값이 존재한다면 return

        # 브라운의 현재 시간 기준 다음 시간의 모든 경우의 수를 BFS로 구한다
        for i in range(0, len(queue)): # while 문을 쓰지 않은 이유는 코니와 매 초 비교하기 위해서
            current_location, current_time = queue.popleft()

            # 다음 시간에 브라운이 위치할 3가지 패턴을 모두 경우의 수로 넣어준다
            new_time = current_time + 1
            new_location = current_location - 1
            if 0 <= new_location <= 200000: # 브라운의 범위 제한
                visited[new_location][new_time] = True # 해당 위치, 해당 시간을 방문했다는 기록
                queue.append((new_location, new_time))

            new_location = current_location + 1
            if 0 <= new_location <= 200000:
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))

            new_location = current_location * 2
            if 0 <= new_location <= 200000:
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))

        time += 1 # 코니의 시간도 더해준다

    return time


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))