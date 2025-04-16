class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head   tail
# [6] -> [3]
# 2 추가
# head          tail
# [6] -> [3] -> [2]

# 즉 queue에 데이터를 넣으면 head는 처음 들어온 값이 고정되고 tail 은 새로 들어온 값으로 교체된다

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)  # 새로운 노드 만들고
        # 맨 처음 추가하는 경우라면 예외 처리
        if self.is_empty():  # 만약 비어있다면,
            self.head = new_node  # head 에 new_node를
            self.tail = new_node  # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node # 맨 마지막으로 넣어주고
        self.tail = new_node # 새로운 노드를 tail 로 임명

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data # 맨 앞에 있는 값

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(2)
queue.enqueue(3)