# Q. 네트워크

# <문제분석>
# A와 B가 직접, B와 C가 직접 연결이면 A-C도 연결
# 이런 관계가 같은 네트워크 상에 있다고 함

# 컴퓨터 개수 n
# 연결 정보 2차원 배열 computers
# -> 네트워크의 개수 return
# 1 <= n <= 200
# 컴퓨터는 0부터 n-1 인 정수로 표현
# computers[i][j] 를 1로 표현하면 연결된 것

# <풀이>
# n개의 각 컴퓨터를 뽑아서
# visited 에 넣고
# 연결된 것들 visited에 담으면 됨
# BFS

# [1, 1, 0]
# [1, 1, 0]
# [0, 0, 1]

def solution(n, computers):
    answer = 0

    visited = [False] * n

    def dfs(node):
        visited[node] == True
        for next_node in range(n):
            if not visited[next_node] and computers[node][next_node] == 1:
                visited[next_node] = True
                dfs(next_node)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer