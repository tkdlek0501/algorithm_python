# Q. 완주하지 못한 선수
# 해시 문제

# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
# 입출력 예 설명
# 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
#
# 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
#
# 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.


# <문제분석>
# 단 한 명 제외하고 모든 선수가 완주
# 이름이 담긴 배열 : participant
# 완주한 선수 이름이 담긴 배열 completion
# 완주하지 못한 선수의 이름을 return

# 100,000 이하
# 이름은 알파벳 소문자
# 동명이인이 있을 수 있다

def solution(participant, completion):
    answer = ''
    dict = {}

    for key_p in participant:
        if key_p in dict:
            dict[key_p] += 1
        else:
            dict[key_p] = 1

    for key_c in completion:
        if key_c in dict:
            dict[key_c] -= 1

    for key in dict:
        if dict[key] >= 1:
            return key

    return answer

# <피드백>
# 아래처럼 collections 의 Counter를 사용하여 빼기가 가능하다
# dict의 keys() 를 꺼내 list로 만들고 그 중 0번째를 꺼내면 한 사람이 추출된다
import collections
def solution1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 내 풀이가 잘못된 것은 아니고, 개선하자면
# if문 사용을 줄이기 위해
# dict.get(key, 0) 을 통해 default를 0으로 설정할 수 있다
# 또한 dict에 들어가는 값이 key, value 형식이므로
# dict.items() 를 하면 key, value를 동시에 꺼낼 수 있다
def solution2(participant, completion):
    counter = {}

    for p in participant:
        counter[p] = counter.get(p, 0) + 1

    for c in completion:
        counter[c] -= 1

    for name, count in counter.items():
        if count > 0:
            return name