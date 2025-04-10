# TODO: 두 링크드 리스트의 합산 구하기
# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때,
# 합산한 값을 반환하시오.
#
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.
#
# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.

# [6] -> [7] -> [8]
# [3] -> [5] -> [4]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

# 아이디어
# 링크드 리스트에 있는 숫자의 합은 앞에서 부터 꺼내서 만들어 줘야 한다
# ex. 6 -> 7 -> 8 이 678이 되기 위해서는
# '들어가 있는 값' * 10 + '더해주려고 하는 값' 형식으로 자리에 맞게 넣어줄 수 있다

def get_linked_list_sum(linked_list_1, linked_list_2):

    # 1. 링크드 리스트로 들어간 원소를 ex. 678 형식으로 만들어 줘야 한다
    # 2. 앞에부터 꺼내서 들어가니까 넣을 때마다 기존에 들어간 값을 *10 해주고 다음 숫자를 더해주면 된다
    sum_1 = get_sum_by_linked_list(linked_list_1)
    sum_2 = get_sum_by_linked_list(linked_list_2)

    return sum_1 + sum_2

def get_sum_by_linked_list(linked_list):
    sum = 0
    cur = linked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next
    return sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))