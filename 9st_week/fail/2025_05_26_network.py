# Q. 네트워크
#
# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
#
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#
# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.
# 입출력 예
# n	computers	return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1


def solution(n, computers):
    visited = [False] * n # 컴퓨터 개수만큼 방문지

    def dfs(node): # 그 네트워크 상에 모든 정보 기록
        visited[node] = True # 해당 노드 방문
        for next_node in range(n):
            if computers[node][next_node] == 1 and not visited[next_node]:
                # 지금노드와 다음노드가 연결되어있고 방문하지 않았으면
                dfs(next_node)

    answer = 0
    for i in range(n):
        if not visited[i]: # i 노드 기준으로 새로운 네트워크 탐색
            dfs(i)
            answer += 1

    return answer

# <피드백>
# visited 배열을 이용하여 방문지를 기록해야 한다
# 네트워크는 연결되어 방문한 집합으로 볼 수 있기 때문
# 방문했다면 그건 하나의 네트워크에 포함되므로 초기화 하지 않는다

