# Depth First Search

# DFS 구현해보기 - 재귀함수

# 갈 수 있는 만큼 깊이 탐색하다가 끝에 도달하면 다른 방향으로 다시 탐색하는 구조
# 방문하지 않은 원소를 계속 찾아가면 된다

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

# 1. 시작 노드인 1부터 탐색
# 2. 현재 방문한 노드를 visited_array 에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 반환
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    print(adjacent_graph.get(cur_node)) # 1이면 [2,5,9]
    for adjacent_node in adjacent_graph.get(cur_node):
        dfs_recursion(adjacent_graph, adjacent_node, visited_array) # 재귀

    return
# 하지만 모든 경우의 수를 탐색하는 방법으로 재귀를 이용하는 것은 좋지 않다
# 너무 많은 반복이 실행되면 RecursionError가 발생할 수 있다
# 가장 마지막에 위치한 노드까지 탐색하는 것이므로 스택을 이용하면 된다


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!