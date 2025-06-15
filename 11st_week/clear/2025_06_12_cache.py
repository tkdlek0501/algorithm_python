# Q. 캐시

# <문제분석>
# 캐시 크기에 따른 실행 시간 측정 프로그램 작성

# 캐시 크기 cacheSize <= 30
# 도시이름 배열 cities 문자열 배열이고 100,000개 까지
# 각 도시 이름은 공백, 숫자, 특수문자 등 없이 영문자로 구성
# 대소문자 구분 안하고 최대 20자

# 도시이름 배열을 순서대로 처리할 때 총 실행시간 출력

# 캐시 교체 알고리즘은 LRU 를 사용하고?
# cache hit 이면 실행시간 1
# cache miss 이면 실행시간 5
# cache는 선입선출되니까 queue로 관리?

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    for city in cities:
        city = city.lower()

        if city in cache:
            # Cache hit
            cache.remove(city) # 제거하고
            cache.append(city) # 다시 넣음
            answer += 1
        else:
            # Cache miss
            if cacheSize > 0 and len(cache) >= cacheSize:
                cache.popleft() # 마지막 것 제거
            if cacheSize > 0:
                cache.append(city) # 캐시에 넣음
            answer += 5

    return answer

# <피드백>
# LRU는 가장 오래 전에 사용된 데이터를 제거하는 캐시 교체 알고리즘
# cache hit 일 때도 원래 것 제거하고 맨 마지막에 다시 밀어 넣는다
# cache miss 일 때는 개수가 가득 찼을 때는 제거하고 넣고
# 아니면 그냥 넣는다

# queue 에서 특정 원소 제거는 remove() 쓸 수 있다