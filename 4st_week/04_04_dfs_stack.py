# DFS 구현해보기 - 스택 (재귀 방식은 안좋다!)
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

# 1. 시작 노드를 스택에 넣는다
# 2. 현재 스택의 노드를 빼서 visited 에 추가한다
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가한다
# 위의 과정을 스택이 빌 때까지 반복

def dfs_stack(adjacent_graph, start_node):
    stack = [start_node] # [1]
    visited = []
    while stack: # 스택이 비어 있지 않은 동안
        current_node = stack.pop() # 스택에서 마지막 요소를 꺼낸다
        visited.append(current_node) # 방문한 노드로 넣어준다
        for adjacent_node in adjacent_graph[current_node]: # 인접한 노드들
            if adjacent_node not in visited: # 방문하지 않았으면
                stack.append(adjacent_node) # 스택에 넣어준다

    return visited

# 이해를 해보자면
# 처음에 1부터 시작해서
# 그 다음 인접 노드들을 찾아와주고 스택에 넣어준다
# 그 중 마지막 요소에 대해서
# 또 인접 노드들을 찾아와주고 스택에 넣어주는 것을 반복
# 스택에서 마지막 요소를 꺼내주면서 없어질 때 까지 진행


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!