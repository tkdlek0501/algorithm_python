# Q. 영어 끝말잇기

# <문제분석>
# 1부터 n까지 번호가 붙어있는 n명의 사람
# 영어 끝말잇기
# 1. 1번 부터 번호 순서대로 단어 말함
# 2. 마지막 사람이 단어를 말하면 다시 1번부터 시작
# 3. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어 말해야 함
# 4. 한 번 사용한 단어 재사용 안됨
# 5. 한 글자 단어는 인정되지 않음

# ex. 3명
# tank -> kick -> know ->  ....

# 사람의 수 n
# 사람들이 순서대로 말한 단어 words가 주어질 때
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지 return
# [3, 3]

# <풀이>
# for 문 돌아서 임의 배열에 있는지 확인
# + 이어지지 않는 단어 말하면 탈락
# i 번째 라면 n으로 나눠서 몫은 회차고 나머지에 해당하는 사람이 탈락

def solution(n, words):

    arr = []
    for i in range(len(words)):
        if i != 0:
            if words[i] in arr or words[i][0] != arr[-1][-1]:
                return [i % n + 1, i // n + 1]  # 1부터 시작하므로 +1
        arr.append(words[i])

    return [0, 0]