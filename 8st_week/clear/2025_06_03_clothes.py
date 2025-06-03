# Q. 의상

# <문제분석>
# 종류(한개) / 의상 이름(여러개)

# 각 종류별로 최대 1가지 의상만 착용 가능
# ex.
# 같은 종류에서는 여러개 착용 불가

# 일부 겹치더라도 다른 의상이 겹치지 않거나 혹은 의상을 추가로 더 착용하면 조합 가능
# 하루에 최소 한 개 의상은 입음

# <풀이>
# 각 종류별로 동시에 입어야 하고
# 최소 한 개의 의상을 입어야 하므로 모두 안 입는 조합은 불가


def solution(clothes):  # [의상, 종류] - value, key
    answer = 1

    clothes_dic = {}

    for clothe in clothes:
        if clothe[1] in clothes_dic:
            clothes_dic[clothe[1]] += 1
        else:
            clothes_dic[clothe[1]] = 1

    for key in clothes_dic:
        answer *= clothes_dic[key] + 1

    return answer - 1