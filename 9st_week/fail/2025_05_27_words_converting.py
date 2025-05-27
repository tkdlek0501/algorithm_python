# Q. 단어 변환
#
# 문제 설명
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
#
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
#
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.
# 입출력 예
# begin	target	words	return
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
# 입출력 예 설명
# 예제 #1
# 문제에 나온 예와 같습니다.
#
# 예제 #2
# target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.

# <문제분석>
# 두 개의 단어 begin, target
# 단어 집합 words

# begin -> target 으로 변환하는 가장 짧은 변환 과정을 찾으려 한다 -> BFS
# 규칙
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있다
# 2. words 에 있는 단어로만 변환할 수 있다

# ex.
# begin : hit / target : cog
# word : ["hot", "dot", "dog", "lot"..., "cog"]
# hit -> hot -> dot -> dog -> cog // target인 cog 까지 4 단계 걸림

# <풀이>
# 모든 변환 가능한 경우의 수를 구해서 cog인지 확인하고 가장 짧은 count을 반환
# BFS 니까 queue에다가 값 담기? word에 있는 걸로만 변환 가능하다

from collections import deque


def is_convertible(word1, word2):  # 두 단어가 한 글자만 다른지 체크하는 함수
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    return count == 1


def solution(begin, target, words):
    if target not in words:  # words 에 target 이 존재하지 않으면 target 도달 불가
        return 0

    visited = set()  # 이미 변환된 단어는 제외
    queue = deque()
    queue.append((begin, 0))  # (현재 단어, 단계 수)

    while queue:
        current_word, step = queue.popleft()

        if current_word == target:
            return step

        for word in words:
            if word not in visited and is_convertible(current_word, word):  # 아직 거치지 않았고 변환이 가능하다면
                visited.add(word)
                queue.append((word, step + 1))

    return 0  # target에 도달하지 못한 경우


from collections import deque

# 다시 혼자 풀이
def solution1(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))  # 단어, 변환 횟수
    visited = []

    while queue:
        word, count = queue.popleft()

        if target == word:  # target 도달하면 count 반환
            return count

        # queue에 append
        # 1. visited 방문 안한 것
        # 2. 단어가 하나만 다른 단어
        for w in words:
            if w not in visited and is_possible_word(word, w):
                queue.append((w, count + 1))
                visited.append(w)

    return 0


def is_possible_word(word1, word2):
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
    return count == 1  # 다른게 하나만 존재하면 변환 가능

# <피드백>
# visited를 리스트 말고 set으로 바꾸면 더 빠름
# 리스트에서 in 연산은 O(N)
# set은 O(1)
# visited를 계속 배열로 만드는 걸로 익숙해졌는데 set이 더 유리하다
# visited = set() 하고 visited.add(w) 로 요소 추가 가능