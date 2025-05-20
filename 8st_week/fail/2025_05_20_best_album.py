# Q. 베스트앨범
# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.
# 입출력 예
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
# 입출력 예 설명
# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
#
# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생
# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
#
# 고유 번호 4: 2,500회 재생
# 고유 번호 1: 600회 재생
# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.
#
# 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.

# <문제분석>
# 장르 별로 가장 많이 재생된 노래 두 개씩 모아 베스트 앨범 출시
# 노래는 고유 번호로 구분
# *노래를 수록하는 기준
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생 횟수가 같은 노래이면 고유 번호가 낮은 노래 먼저 수록

# 장르를 나타내는 문자열 배열 genres
# 노래별 재생 횟수를 나타내는 정수 배열 plays
# 베스트 앨범에 들어갈 노래의 고유 번호 순서대로 return
# genres와 plays의 길이는 같음

# <풀이>
# 장르, 고유번호, 재생횟수 알아야 한다
# -> 해시) key : 장르, value : {key: 고유번호, value: 재생횟수}, ...
# 장르별 속한 노래가 많이 재생됐는지 확인해야 하므로 따로 계산 필요
# -> 해시) {key : 장르, value : 재생횟수}, ...
# 재생횟수 값으로 정렬 필요해서 compare 필요

def solution(genres, plays):
    answer = []

    genre_play_sum_dict = {}  # 장르별 재생횟수 합
    genre_play_dict = {}  # 장르별 노래 정보
    idx = 0
    for genre, play in zip(genres, plays):
        genre_play_sum_dict[genre] = genre_play_sum_dict.get(genre, 0) + play
        if genre not in genre_play_dict:
            genre_play_dict[genre] = {}
            genre_play_dict[genre][idx] = play
        else:
            genre_play_dict[genre][idx] = play
        idx += 1

    # print(genre_play_sum_dict)
    # print(genre_play_dict)

    # 장르별 재생횟수 합 기준으로 가장 많이 재생된 장르부터 정렬
    sorted_genre_play_sum_dict = sorted(genre_play_sum_dict.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_genre_play_sum_dict)

    for genre, play in sorted_genre_play_sum_dict:
        sorted_genre_play_dict = sorted(genre_play_dict[genre].items(), key=lambda item: item[1], reverse=True)
        # print(sorted_genre_play_dict)
        count = 0
        for idx, value in sorted_genre_play_dict:
            if count >= 2:
                break
            answer.append(idx)
            count += 1

    return answer

# <피드백>
# 중간중간 내가 원하는 결과를 만들어 냈는지 print를 찍어보며 진행하는 건 좋다
# 자료구조를 어떤 형식으로 쓸지 적어놔서 헷갈리지 않게 하는 게 좋다
# 여기서 핵심은
# dict 안에 dict가 들어있는 2중 dictionary 사용법
#         if genre not in genre_play_dict:
#             genre_play_dict[genre] = {}
#             genre_play_dict[genre][idx] = play
# 그리고 그 값을 가지고 sort 하는 lambda 식 사용법
# sorted(genre_play_dict[genre].items(), key=lambda item: item[1], reverse=True)