# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때,
# 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.

# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

# menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
# orders = ["오뎅", "콜라", "만두"]

# Tip. array = [4, 1, 6, 2] 를 정렬하는 방법
# array.sort() 쓰면 오름차순으로 정렬됨

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 아이디어
# 주문한 메뉴가 가능한 메뉴에 포함 돼있는지를 알아야 한다
# 두 메뉴 리스트는 배열로 들어온다
# 빠르게 탐색 하려면 가장 효율적인 방법인 이진 탐색을 이용해서 풀어보자
# 이진 탐색의 전제 조건은 정렬이 되어 있어야 한다는 것이다
# 하지만 아래와 같은 방법은 시간복잡도를 계산해봤을 때 효율적이지 않다
def is_available_to_order(menus, orders):
    # O(NlogN) + O((N+M)log(N))
    menus.sort() # O(NlogN)
    for order in orders: # O(M)
        if not is_exist_target_number_binary(order, menus): # O(logN)
            return False
    return True

def is_exist_target_number_binary(target, array):
    current_index = (len(array) - 1) // 2
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        if array[current_index] == target:
            return True
        else:
            if target > array[current_index]:
                left_index = current_index + 1
            else:
                right_index = current_index - 1
        current_index = (left_index + right_index) // 2
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)