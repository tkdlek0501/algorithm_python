# Q. 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다.
# 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다.
#
# 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다.
# 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
#
# 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고,
# 6번 좌석이나 8번 좌석에도 앉을 수 있다.
# 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.
#
# 그런데 이 극장에는 “VIP 회원”들이 있다.
# 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.
#
# 예를 들어서,
# 그림과 같이 좌석이 9개이고,
# 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다.
# 또한 <213465789> 와 <132465798> 도 가능한 배치이다.
# 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.
#
# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다.
# 총 좌석의 개수와 VIP 회원들의 좌석 번호들이 주어졌을 때,
# 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 반환하시오.

# 문제 분석
# 고정 좌석이라는 개념이 있다
# ex. 123 [4] 56 [7] 89
# 123 56 89 가 어떻게 옮길 수 있는지 경우의 수를 구해야 한다

# 1. 숫자를 써보면서 발견해보기 -> 쉽지는 않다
# [1, 2] -> [1, 2][2, 1]
# [1, 2, 3] -> [1, 2, 3][2, 1, 3][1, 3, 2]
# [1, 2, 3, 4] -> [1, 2, 3, 4][1, 2, 4, 3][1, 3, 2, 4][2, 1, 3, 4][2, 1, 4, 3]
# 피보나치 수열을 쓰면 된다
# 2. 점화식을 통해 파악
# 1 2 3 ... n-2 n-1 n
# n 번째 티켓을 가진 사람이 앉을 수 있는 방법 (2가지 뿐이다)
# 1. n 번째 좌석에 앉는다
# -> 좌석은 n-1 개 남아있고, 사람도 n-1 번째 티켓까지 가진 사람이 있는 상황
# => N-1 명의 사람을 좌석에 배치하는 방법 = F(N-1)
# 2. n-1 번째 좌석에 앉는다
# -> n-1 번째 티켓을 가진 사람은 n번째 좌석에 앉아야 한다
# -> 좌석은 n-2 개가 남아있고 사람도 n-2 번째 티켓까지 가진 사람이 있는 상황

# tip) 이런 문제가 피보나치를 이용해야 될 거라고 파악하기 쉽지 않다
# 어떤 규칙성을 가지긴 하겠다까지는 접근해도 피보나치를 써야 한다까지는 어렵다
# 이런 문제 패턴에 대해 익혀서 감을 잡아야 한다

# F(N) 이 N 명의 사람들을 좌석에 배치하는 방법이라고 하면
# F(N) = F(N-1) + F(N-2)

# 3 x 2 x 2 = 12
# f(3) f(2) f(2)
# 123 4 56 7 89

# 피보나치 수열 구하는 방법
memo = {
    1: 1,
    2: 2 # 여기서는 f(2) 가 2이므로 1이 아니라 2여야 한다
}
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo


seat_count = 9
vip_seat_array = [4, 7]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1 # 최소 경우의 수
    current_index = 0

    # 고정 좌석 기준으로 그 전의 좌석들의 경우의 수를 구해서 곱의 법칙에 따라 곱해줌
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways # 총 경우의 수는 각각의 경우가 동시에 일어나므로 곱의 법칙
        current_index = fixed_seat_index + 1
    # 마지막 고정 좌석 이후의 좌석
    all_ways *= fibo_dynamic_programming(total_count - current_index, memo)

    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))