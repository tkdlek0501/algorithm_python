class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 시간복잡도 O(log(N)) ;루트 노드부터 리프 노드까지 길이
    # 맨 위의 루트 노드의 값을 제거하기 위해서는
    # 1. root와 맨끝 노드의 위치를 바꾼다
    # 2. 그리고 바뀐 root 노드를 자식과 비교한다
    # 3. 자식들이 크다면, 둘 중 더 큰 자식과 위치를 바꾼다
    # 4. 이 과정을 리프 노드에 도달하거나 자식보다 클 때까지 반복한다
    # 5. 그리고 1번 root 노드를 반환
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop() # 이전 최대값을 미리 pop 해둔다

        cur_index = 1
        while cur_index <= len(self.items) - 1: # 현재 items의 맨 끝 인덱스에 도달하기 전까지
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            # 자식 노드 인덱스의 범위는 최대 인덱스 이하여야 하고, 그 값이 부모 보다 클 때까지만 반복
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if cur_index == max_index: # 현재 인덱스가 max_index와 변함이 없으면 자식이 더 큰 값 없는 것이므로 break
                break

            # 값의 위치를 바꿔주고
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            # 자식 노드 인덱스로 값이 이동 했으므로 새로운 max 인덱스로 대입
            cur_index = max_index

        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]