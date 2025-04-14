# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.

# [6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때,
# 끝에서 2번째 값은 7을 반환해야 합니다!

# 아이디어
# 링크드 리스트는 head 부터 순차적으로 값을 탐색할 수 있다
# -> 뒤에서부터 탐색하는 것은 불가하다
# 대신 size 를 알 수는 있다
# 즉 총 길이를 이용해서
# 만약 4자리중 뒤에서 2번째 요소를 찾으라고 한다면
# 앞에서 부터는 3번째 요소이니까 4 - (2 - (1)) 에 해당하는 위치의 요소를 찾으면 된다

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

    # def get_kth_node_from_last(self, k):
    #     # 총길이 구하기
    #     total_size = 1
    #     cur = self.head
    #     while cur.next is not None:
    #         total_size += 1
    #         cur = cur.next
    #     # 길이값 계산
    #     # 총자리가 4자리라면 뒤에서 2번째는 앞에서 3번째
    #     # 인덱스로 계산하면 4 - 2 번째 인덱스
    #     search_index = total_size - k
    #
    #     # getNode
    #     cur_index = 0
    #     cur = self.head
    #     while cur_index != search_index:
    #         cur = cur.next
    #         cur_index += 1
    #
    #     return cur

# 또 다른 방법
# 우리는 끝에서 k번 째인 노드의 값을 알고 싶은 거다
# 즉 2개의 slow, fast 라는 탐색을 사용해서 한 번의 순환 안에 찾을 수 있다
# 예시(k=2)
# head
# slow         fast
#       slow           fast
#              slow           fast
#                     slow            fast
# [6] -> [7] -> [8] -> [9] -> [10] -> [11]
# 위 처럼 fast 가 끝에 다달았을 때 우리가 알고 싶은 값은 slow에 위치하게 된다
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow
# 하지만 2N에서 N으로 줄였다고 해도 O(N) 만큼의 시간복잡도를 가지는 것은 동일하므로
# 시간복잡도가 크게 차이나지는 않는다


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!