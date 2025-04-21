class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 시간복잡도 = O(log(N)) ;최악의 경우(루트 노드까지 가게되는 경우) 완전 이진 트리의 최대 높이와 동일
    def insert(self, value):
        # 우선 가장 마지막에 값을 넣는다
        # 부모 노드를 찾으며 바꿔야 한다
        # 부모 노드의 값이 더 크거나 루트 노드에 달하면 멈춘다
        self.items.append(value)

        cur_index = len(self.items) - 1 # 맨 마지막 인덱스 = 배열의 길이 - 1

        while cur_index != 1: # 1이면 루트 노드이기 때문에 1이 아닐 때까지
            # 부모 노드와 비교해서 더 크면 위치를 바꾼다
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break

        return

# 완전 이진 트리
#           8       Level 0
#         6   3     Level 1
#        4 2 5      Level 2
# [None, 8, 6, 3, 4, 2, 5]

# 부모 노드의 왼쪽 자식은 부모 노드 level * 2
# 부모 노드의 오른쪽 자식은 부모 노드 level * 2 + 1

# max heap insert 의 과정
# 1. 완전 이진 트리의 맨 뒤에다가 원소를 넣는다.
# 2. 부모와 비교해서 자기가 크면 위치를 바꾼다.
# 3. 2번의 과정을 부모가 더 크거나 루트 노드에 달했을 때 까지 반복한다.

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
#     3     Level 0
#    4      Level 1
# 3과 4 비교했을 때 자식인 4가 더 크므로 위치를 바꿔준다
#     4     Level 0
#    3      Level 1
# 4가 루트 노드에 달했으므로 멈춘다

# -> [None, 3, 4]
# -> 부모의 인덱스를 구하려면 2 // 2 나눠서 내린 수 = 1
# -> 즉 부모 인덱스(1) vs 자식 인덱스(2)
# => [None, 4, 3]
max_heap.insert(2)
#     4     Level 0
#    3 2    Level 1
# 2가 부모인 4보다 작으므로 아무런 추가 동작을 하지 않는다

# -> [None, 4, 3, 2]
max_heap.insert(9)
#     4     Level 0
#    3 2    Level 1
#   9       Level 2
# 자식인 9가 부모인 3보다 크므로 자리를 바꾼다
#     4     Level 0
#    9 2    Level 1
#   3       Level 2
# 자식인 9가 부모인 4보다 크므로 자리를 바꾼다
#     9     Level 0
#    4 2    Level 1
#   3       Level 2
# 9가 루트 노드에 달했으므로 멈춘다

# -> [None, 4, 3, 2, 9]
# -> 9(4번째 인덱스)의 부모 노드의 인덱스는 4 // 2 = 2
# -> 3(i = 2) vs 9(i = 4)
# -> [None, 4, 9, 2, 3]
# -> 9(2번째 인덱스)의 부모 노드의 인덱스는 2 // 2 = 1
# -> 4(i = 1) vs 9(i = 2)
# -> [None, 9, 4, 2, 3]
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!