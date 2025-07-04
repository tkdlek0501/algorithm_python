# Q. 모음 사전
#
# 문제 설명
# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
#
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
# 입출력 예
# word	result
# "AAAAE"	6
# "AAAE"	10
# "I"	1563
# "EIO"	1189
# 입출력 예 설명
# 입출력 예 #1
#
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다. "AAAAE"는 사전에서 6번째 단어입니다.
#
# 입출력 예 #2
#
# "AAAE"는 "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU"의 다음인 10번째 단어입니다.
#
# 입출력 예 #3
#
# "I"는 1563번째 단어입니다.
#
# 입출력 예 #4
#
# "EIO"는 1189번째 단어입니다.


# <문제분석>
# 'A', 'E', 'I', 'O', 'U'
# 길이 5 이하의 모든 단어가 수록돼있다

# 사전에서 첫 번째 단어는 A 그 다음 AA 마지막은 UUUUU

# 단어 하나 word가 매개변수로 주어질 때 이 단어가 사전에서 몇 번째 단어인지 return

def solution(word):
    words = []
    chars = ['A', 'E', 'I', 'O', 'U']

    def dfs(current):
        if len(current) > 5: # current 단어의 길이 제한
            return
        if current: # current가 있을 때 append
            words.append(current)
        for ch in chars: # current 단어에 ch를 하나씩 추가
            dfs(current + ch)

    dfs("")  # 빈 문자열부터 시작
    words.sort()
    return words.index(word) + 1

# 피드백
# 각 자리 문자 중복이 가능해서 permutaions 를 이용한 순열로는 풀 수 없다
# 모든 단어에 대해서 만들고 탐색해야 하는 문제 (완전탐색)
# -> dfs 로 재귀적으로 모든 단어를 만들 수 있다
# dfs 를 이용해서 직접 모든 단어를 만들어 줘야 한다