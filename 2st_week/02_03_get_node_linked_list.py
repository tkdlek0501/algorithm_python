class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

# LinkedList 의 가장 끝에 있는 노드에 새로운 노드를 연결하기
    def append(self, value):
        cur = self.head
        while cur.next is not None: # next 의 값이 None 이라면 마지막 Node
            cur = cur.next
        cur.next = Node(value)

    # linked_list 에 저장한 head 를 따라가면서 현재 있는 Node 들을 전부 출력해주는 함수
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

linked_list = LinkedList(5)
linked_list.append(12)

# 1. 특정 인덱스(노드) 원소를 찾기
# 링크드리스트에서 특정 노드에 접근하기 위해서는 반드시 헤드에서 출발해야 된다는 점을 알자.
print(linked_list.get_node(0).data)
print(linked_list.get_node(1).data)
