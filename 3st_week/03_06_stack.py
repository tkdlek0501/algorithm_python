# 스택 자료구조
# 스택은 Last In First Out LIFO 방식으로 돼있는 자료구조이다
# 즉 마지막에 넣은게 처음으로 나간다
# 빨래통에 빨래 넣고 빼는 것을 생각해도 되고 접시를 쌓고 빼는 것을 생각해도 된다 이미지화 하자

# 스택도 결국 각 노드를 빼고 넣고 할 수 있기 때문에 링크드리스트와 유사하게 구현할 수 있다

# ex.
# [4] -> [3]
# 위처럼 쌓는다면 pop() 하면 마지막 3이 뽑혀야 한다
# 즉 스택에서 중요한 것은 맨 위에 있는 값, head 이다 head 에 있는 값을 뺄거냐 새로운 값을 head로 넣을거냐 이다
# 데이터를 쌓을 때 head로 넣어주도록 하면 효율적인 자료구조로 만들 수 있게 된다

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value) # 새로운 head
        new_head.next = self.head # 새로운 head에 기존 것 붙이기
        self.head = new_head # 새로운 head를 이 Stack의 head로 만들기
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty(): # 주의: Node를 제거할 때는 더 이상 제거하지 못하는 예외 상황에 대해서 생각해야 한다
            return "stack is Empty"

        delete_head = self.head
        self.head = self.head.next # next를 head로 만들어준다
        return delete_head

    def peek(self):
        if self.is_empty(): # 주의: Node를 제거할 때는 더 이상 제거하지 못하는 예외 상황에 대해서 생각해야 한다
            return "stack is Empty"

        return self.head.data # peek은 값을 바로 반환

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())