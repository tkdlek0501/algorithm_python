# Q. 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고,
# r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.
#
# 이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다.
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
#
# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
#
# 예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.
#
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 2
#
# 0은 빈 칸, 1은 집, 2는 치킨집이다.
#
# (2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.
#
# (5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.
#
# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다.
# 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.
#
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 반환하시오.
#
# 입력
# N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
# 또한 도시의 정보가 주어진다.
#
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.
#
# 출력
# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때,
# 도시의 치킨 거리의 최솟값을 출력한다.


# <문제분석>
# 크기가 N x N 인 정사각형 도시가 있다
# 1 x 1 의 칸으로 나눠져 있다
# 도시의 각 칸은 총 3가지로 빈 칸, 집 칸, 치킨집 칸 이 있다
# 도시의 칸은 (r, c) 로 나타낸다 각 행, 열을 의미한다 + r과 c는 1부터 시작한다 (0이 아니다!)
# "치킨거리"? 집과 '가장 가까운' 치킨집 사이의 거리, 각 집은 치킨 거리를 갖고 있다
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다 -> 겹쳐도 합치는 건가?
# 두 칸 사이의 거리는 |r1-r2| + |c1-c2| 로 구한다
# 0은 빈 칸, 1은 집, 2는 치킨집이다
# 폐업시키는 게 목적이고 수익을 많이 낼 수 있는 치킨집의 개수는 M개 라고 한다
# 도시에 있는 치킨집 중에서 최대 M개 고르고 나머지 치킨집은 모두 폐업시켜야 한다 어떻게 골라야 도시의 치킨 거리가 가장 작게 될까를 반환해야 한다
# 폐업시키지 않을 치킨집을 M 이라고 표현하고 도시의 치킨 거리의 최솟값을 출력해야 한다

# <문제풀이>
# * r과 c는 0이 아닌 1부터 시작한다 (인덱스와 다르다)
# 0. 주어지는 map 각 칸은 0, 1, 2 로 각각 빈 칸, 집 칸, 치킨집 칸
# 1. 입력되는 N 값으로 정사각형 2차원 배열을 N x N 개로 만든다
# 2. 각 칸에 어떤 정보를 담을까? ->
# 3. 치킨 거리가 가장 작게 되는 것을 구하려면 모든 경우의 수를 봐야 한다. 기준이 각 집이므로 어떤 경우가 더 짧은지 판단할 수 있는 근거가 없다
# 4. 모든 경우의 수? -> 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같아야 하므로 폐업시키지 않을 치킨집이 최대 M개니까 M 개 이하에서 모든 경우의 수를 구해야 한다?
# M(폐업시키질 않을 최대 치킨집 수) <= 치킨집(2) <= 13

# <구현>
# tip)
# 1. 조합을 얻으려면
# >>> from itertools import combinations
# >>> itertools.combinations([1,2,3,4,5], 2) # [1,2,3,4,5] 에서 2개씩 뽑을 수 있는 조합을 다 가져와라
# <itertools.combinations object at 0x10453acc0>
# >>> list(itertools.combinations([1,2,3,4,5], 2))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
# >>> list(itertools.combinations([1,2,3,4,5], 3))
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
# 2. 숫자의 최댓값을 얻으려면? -> 구하고자 하는 게 최솟값이므로
# >>> from sys
# >>> min_value = sys.maxsize
# >>> min_value
# 9223372036854775807



import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

# 여러개 중 M개를 골라야 한다
# 그 치킨 거리가 가장 작게 되는 경우 -> 모든 경우의 수 다 봐야 한다
# 치킨 거리 값 구하려면 치킨 집과 집의 위치를 다 가져와서 그 거리의 합을 구해야 한다
def get_min_city_chicken_distance(n, m, city_map):

    # 1. 치킨집과 집의 위치 정보 저장해놓기
    chicken_location_list = [] # 치킨 집 위치 정보
    home_location_list = [] # 집 위치 정보
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1: # 집 이면
                home_location_list.append([i, j])
            elif city_map[i][j] == 2: # 치킨집이면
                chicken_location_list.append([i,j])
    # print("home_location_list : ", home_location_list)
    # print("chicken_location_list : ", chicken_location_list)

    # 2. 치킨집 중에 남길 치킨집(m개)의 조합을 뽑아오기
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    # print("chicken_location_m_combinations : ", chicken_location_m_combinations)
    min_distance_of_m_combinations = sys.maxsize # 치킨집 조합 중 가장 짧은 치킨 거리 값(result)
    for chicken_location_m_combination in chicken_location_m_combinations: # for 치킨집 조합들을 돌면서
        chicken_location_m_combination_total_chicken_distance = 0 # 이 조합에서 치킨 거리(합)
        # print("chicken_location_m_combination : ", chicken_location_m_combination)
        for home_r, home_c in home_location_list: # for 각 집을 뽑아와서
            # print("home_r, home_c : ", home_r, home_c)
            min_home_chicken_distance = sys.maxsize # 집과 치킨집 간의 거리중 가장 짧은 값 = 그 집의 치킨 거리
            for chicken_location in chicken_location_m_combination: # for 조합 안에서 각각의 치킨집과의 거리 중 최소 거리 구하기
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            chicken_location_m_combination_total_chicken_distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, chicken_location_m_combination_total_chicken_distance)

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))