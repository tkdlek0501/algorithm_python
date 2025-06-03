# Q. 기능개발

# <문제분석>
# 각 기능은 진도가 100% 일 때 서비스 반영 가능
# 각 기능 개발속도 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 가능
# 이 때는 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포

# 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도 적힌 정수 배열 speeds

# 각 배포마다 몇 개의 기능이 배포 되는지 return

# ex.
# [93, 30, 55]
# [1, 30, 5]
# -> [2, 1]

# <풀이>
# 하루마다 speeds 에 따라 퍼센트가 달라진다
# 남아있는 퍼센트 나누기로 계산이 가능?
# ex. 93 이면 7이 남아있고 1로 나누면 7
# 30 이면 70 남아있고 30 으로 나누면 2 + 1
# 55 이면 45 남아있고 5로 나누면 9

# 완료되면 queue에 넣어놓고 앞 작업이 나갈 수 있는지 체크?

from collections import deque


def solution(progresses, speeds):
    answer = []

    queue = deque()  # 각 작업 걸리는 일자

    for p, s in zip(progresses, speeds):
        queue.append(-((p - 100) // s))

    while queue:
        time = queue.popleft()
        count = 1
        while queue and queue[0] <= time:
            queue.popleft()
            count += 1
        answer.append(count)

    return answer