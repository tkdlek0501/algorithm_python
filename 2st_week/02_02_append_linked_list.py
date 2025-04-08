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

linked_list = LinkedList(5)
linked_list.print_all()

linked_list.append(12)
linked_list.print_all()

linked_list.append(8)
linked_list.print_all()
