# Q. 완주하지 못한 선수

# <문제분석>
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤 완주

# 참여한 선수들의 이름이 담긴 배열 participant
# 완주한 선수들의 이름 completion 주어짐
# 완주하지 못한 선수의 이름을 return
# 동명이인이 있을 수 있다

# 풀이
# dictionary 로 key 별로 참여자 인원 수 +1 정리
# completion 돌면서 -1 정리
# value가 1 이상인 참여자 return

def solution(participant, completion):
    answer = ''

    part_dic = {}

    for part in participant:
        if part in part_dic:
            part_dic[part] += 1
        else:
            part_dic[part] = 1
    # print(part_dic)

    for comp in completion:
        if comp in part_dic:
            part_dic[comp] -= 1
    # print(part_dic)

    for pd in part_dic:
        if part_dic[pd] >= 1:
            answer = pd

    return answer