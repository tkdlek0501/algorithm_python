# Q. 스킬트리

# <문제분석>
# 선행 스킬
# ex.
# 스파크 -> 라이트닝 볼트 -> 썬더
# 위 순서에 없는 다른 스킬은 순서에 상관없이 배울 수 있다
# 따라서 힐링이라는 스킬은 언제든 중간에 낄 수 있다

# 선행 스킬 순서 : skill
# 유저들이 만든 스킬트리를 담은 배열 : skill_trees
# 가능한 스킬 트리 개수를 return 하는 함수 작성

# <풀이>
# skill_trees 의 각 스킬을 꺼내면서
# skill 에 있는 값인지 확인 후 처음 것과 비교해 꺼내줘야 한다
# -> 선입 선출 되어야 한다 = queue
# 꺼낼 수 있다면 answer += 1
# 스킬은 중복해 주어지지 않는다
# 스킬은 알파벳 대문자로 표기

from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for s in skill_trees:  # 모든 스킬트리
        skill_queue = deque(skill)  # 선행스킬 queue
        for e in s:  # 각 스킬트리의 스킬들
            if e in skill_queue:  # 스킬이 queue에 있다면
                if e == skill_queue[0]:  # 그 스킬이 선행스킬이 맞다면
                    skill_queue.popleft()  # 꺼내준다
                else:  # 선행스킬이 아니라면
                    break  # 끝
        else:  # for 문을 끝까지 돌았다면
            answer += 1

    return answer