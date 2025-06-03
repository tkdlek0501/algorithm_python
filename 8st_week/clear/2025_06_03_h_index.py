# Q. H-Index

# <문제분석>
# 발표한 논문 n편 중 h 편 이상 인용된 논문이 h 편 이상이고
# 나머지 논문이 h번 이하 인용됐으면 h의 최댓값이 h-index

# 발표한 논문 인용 횟수를 담은 배열 citations

# <풀이>
# 1 ~ n 까지 가능
# h를 바꾸면서 h_index 갱신

def solution(citations):
    h_index = 0

    for h in range(1, len(citations) + 1):
        if sum(1 for citations in citations if citations >= h) >= h:
            h_index = h

    return h_index