# Dictionary 에서의 충돌을 체이닝 방식으로 해결하는 방법

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value): # key, value의 형식으로 배열을 저장
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

linked_tuple = LinkedTuple()

# linked_tuple.add("333", 7)
# linked_tuple.add("77", 6)
#
# print(linked_tuple.items)
#
# print(linked_tuple.get("333"))


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # 해당 item 즉 LinkedTule 에 key, value 형식으로 추가
        # 인덱스 번째 LinkedTuple 은 [(key1, value2), (key2, value2), ..] 형태가 될 것이다.

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


my_dict = LinkedDict()
my_dict.put("test", 0)
print(my_dict.get("test"))