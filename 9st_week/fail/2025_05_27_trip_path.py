# Q. 여행경로
#
# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
#
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
# 입출력 예
# tickets	return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# 입출력 예 설명
# 예제 #1
#
# ["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.
#
# 예제 #2
#
# ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.


# <문제분석>
# 항상 "ICN" 공항에서 출발

# 항공권 정보가 담긴 2차원 배열 tickets
# 방문하는 공항 경로를 배열에 담아 return 해야 함

# 제한사항
# 모든 공항은 알파벳 대문자 3글자
# 주어진 공항 수 3 개 이상, 10,000개 이하
# tickets 의 각 행 [a, b] 는 a에서 b로 가능 항공권이 있다는 의미
# 주어진 항공권은 모두 사용해야 한다
# *만일 가능한 경로가 2개 이상이면 알파벳 순서가 앞서는 경로를 return 해야 한다
# 모든 도시를 방문할 수 없는 경우는 주어지지 않는다

# ex.
# [["ICN","JFK", "HND", "IAD", "JFK","HND"]]
# return : ["ICN","JFK","HND","IAD"]

# <풀이>
# 1. ICN 부터 시작해야 한다
# 2. 현재 위치를 queue로 저장하고, visited 로 방문한 곳 저장
# 3. queue 에 넣을 때 가능한 경로 중 알파벳 순서가 앞서는 경로만 넣어야 한다
# 4. 모든 곳을 다 가야 한다

def solution1(tickets):
    tickets.sort()  # 사전순으로 정렬 (자동으로 가장 빠른 경로부터 탐색됨)
    visited = [False] * len(tickets)
    answer = []

    def dfs(path, used_count):
        if used_count == len(tickets):
            answer.extend(path)
            return True  # 경로를 찾으면 더 이상 탐색하지 않음

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == path[-1]:
                visited[i] = True
                if dfs(path + [tickets[i][1]], used_count + 1):
                    return True  # 경로 찾으면 바로 종료
                visited[i] = False  # 백트래킹

        return False  # 이 경로는 실패

    dfs(["ICN"], 0)
    return answer


from collections import defaultdict


def solution2(tickets):
    graph = defaultdict(list)

    # 그래프 구성 (알파벳 역순으로 정렬 후 stack처럼 pop하기 위해 reverse)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)  # 나중에 경로를 뒤집기 위함

    dfs("ICN")
    return route[::-1]


# <피드백
# BFS 아니고 DFS 에 백트래킹까지 고려해야 한다
# ICN을 여러번 갈 수 있다