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
# 특정 문자열이 배열에 존재하는지만 확인하면 된다
# 정렬 필요없이 집합 자료형을 이용하면 된다
# 집합이란 중복을 허용하지 않는 자료형이다

def is_available_to_order(menus, orders):
    #O(M+N)
    # O(M) + O(N) * O(1)
    menus_set = set(menus) # O(M)
    for order in orders: # O(M)
        if order not in menus_set: # O(1) # set 을 쓰지 않아도 not in 할 수 있긴 한데..
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)