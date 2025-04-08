# TODO: 파이썬에서는 링크드리스트 직접 만들어야 된다. 아래 형식을 익히자.
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

    def add_node(self, index, value):
        new_node = Node(value)

        # index 가 0으로 들어오는 케이스 별도 처리!
        if index == 0:
            # 새로운 헤드를 만들어주고 연결시켜줘야 한다
            new_node.next = self.head
            self.head = new_node
            return

        # n번째 인덱스에 추가한다고 하면 n-1번째 노드의 next 로 연결 지어줘야 한다
        prev_node = self.get_node(index - 1)

        # 기존에 해당 인덱스에 있던 노드를 빼놓는다
        # next_node = self.get_node(index) -> 이렇게도 가능하지만 이전 것 이미 찾았으니 next로 가져오자
        next_node = prev_node.next

        # 새로운 노드를 추가한다
        prev_node.next = new_node

        # 그 뒤에 연결 돼있던 노드를 다시 연결 시켜준다
        new_node.next = next_node

    def delete_node(self, index):
        # 이 때도 0번째 인덱스에 대해서는 별도 처리가 필요하다
        # 1번째에 있는 값을 head 로 올려준다
        if index == 0:
            self.head = self.head.next
            return

        # 인덱스 - 1 의 노드에 인덱스 + 1 의 노드를 바로 연결해주면 된다
        prev_node = self.get_node(index - 1)
        index_node = prev_node.next
        prev_node.next = index_node.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()
print(" ")

# 2. 특정 인덱스(노드) 원소 추가하기
linked_list.add_node(0, 6)
linked_list.print_all()
print(" ")

linked_list.add_node(1, 13)
linked_list.print_all()
print(" ")

linked_list.delete_node(1)
linked_list.print_all()
print(" ")

linked_list.delete_node(0)
linked_list.print_all()