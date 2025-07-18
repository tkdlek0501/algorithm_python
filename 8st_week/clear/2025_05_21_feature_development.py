# Q. 기능 개발
#
# 문제 설명
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
#
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
#
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
#
# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
# 입출력 예
# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
# 입출력 예 설명
# 입출력 예 #1
# 첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
# 두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
# 세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.
#
# 따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.
#
# 입출력 예 #2
# 모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.
#
# 따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.

# <문제분석>
# 진도가 100% 일 때 반영 가능
# 개발속도 모두 다름
# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고
# 이 때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포 된다
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도 정수 배열 speeds
# 각 배포마다 몇 개의 기능이 배포되는 지 return

# ex.
# [93, 30, 55]
# [1, 30, 5]
# -> [2, 1]
# 첫번째 기능은 93% 완료되어 있고 하루에 1% 씩 작업 가능 -> 7일
# 두번째는 30% 완료되어 있고 하루에 30% 씩 작업 가능 -> 3일
# 하지만 이전 기능이 아직 완성 안돼서 7일째 배포
# 세번째는 55% 완료되어있고 하루에 5% 씩 작업해서 9일간 작업 후 배포 가능

# <풀이>
# 하루마다 체크해서 return 가능한 수를 결정해야 한다
# 이전 기능이 완료돼야 다음 기능이 붙어서 나갈 수 있다
# 작업 현재 진도와 스피드 배열은 같은 길이

# 하루 지날 때마다 progress 를 update 해주기
# 모든 progress 가 100% 가 될 때 까지 반복
# 각각 몇일 걸리는 지를 확인해서 담아두기

from collections import deque


def solution(progresses, speeds):
    answer = []

    completed_arr = deque()  # 각 작업이 걸리는 일자
    for progress, speed in zip(progresses, speeds):
        # print(progress, speed)
        completed_arr.append(-((progress - 100) // speed))
    # print(completed_arr)

    # 다음 것이 이전 것의 일자보다 작거나 크면 같이 빼준다
    while completed_arr:
        count = 1
        completed_date = completed_arr.popleft()
        # 나머지중 작은값도 같이 더해주기
        while completed_arr and completed_arr[0] <= completed_date:
            completed_arr.popleft()
            count += 1
        answer.append(count)

    return answer

def solution1(progresses, speeds):
    answer = []

    queue = deque()
    for p, s in zip(progresses, speeds):
        queue.append((p, s))

    while queue:
        count = 1
        p, s = queue.popleft()  # 진행도, 속도
        time = -((p - 100) // s)  # 걸리는 시간

        # 뒤에 있는 작업 중 같이 나갈 수 있는 작업
        while queue and 100 <= queue[0][0] + (time * queue[0][1]):
            queue.popleft()
            count += 1

        answer.append(count)

    return answer

# <피드백>
# 한꺼번에 queue에서 빠져나야 한다라면 while 문을 2번 써서
# 그 차례때 같이 나갈 수 있는 것을 처리해주면 된다
