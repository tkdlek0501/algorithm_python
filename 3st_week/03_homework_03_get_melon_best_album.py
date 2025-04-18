# TODO: Q.멜론 베스트 앨범 뽑기
# 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
#
# 노래는 인덱스로 구분하며, 노래를 수록하는 기준은 다음과 같다.
#
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
#
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
#
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
#
#
# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
#
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.

# 문제분석
# 1. 장르 별로 2 개씩 모아야 됨
# 2. 노래는 인덱스로 구분
# 3. 과정
# 속한 노래가 많이 재생된 장르를 먼저 수록 *단 각 장르에 속한 노래 재생 수 총합은 모두 다르다
# 장르 내에서 많이 재생된 노래를 먼저 수록
# 장르 내에서 재생 횟수가 같으면 고유 번호가 낮은 노래를 먼저 수록
# 장르를 나타내는 문자열 배열 genres
# 노래별 재생 횟수를 나타내는 정수 배열 plays
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환

# 아이디어
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다
# -> genre_array 에서 장르별로 재생횟수를 모두 모아서 비교해준다. 그리고 가장 많이 재생된 장르 별로 노래를 2곡 씩 넣어준다
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다
# -> 많이 재생된 장르 별로 2 곡을 넣어줄 때, 많이 재생된 노래 먼저 넣어줘야 한다
# 3. 장르 내에서 재생횟수가 같다면, 고유 번호 즉 인덱스가 낮은 노래를 먼저 수록해야 한다

# -> '많이', '가장' 등과 같은 키워드가 나오면 '거의' 정렬을 써야 한다

# 풀이방법
# 어떤 값이 오는지 모르기 때문에 특정 key 값 마다 value를 합산할 수 있어야 하므로 dictonary 를 쓴다
# dict = {}   ('장르명','재생수 합')
# -> 어떤 장르가 가장 재생 횟수가 높은지 뽑아낼 수 있다

# 장르 내에서 많이 재생된 노래를 먼저 수록

# 장르별로 총 재생횟수도 저장해야 하지만
# 장르 내에서 각 노래의 재생 횟수도 알고 있어야 한다
# 따라서 데이터를 저장하는 과정은
# 1.
# -> dict = {"classic":500, "pop":600}
# -> dict2 = {"classic":[(0, 500)], "pop":[(1, 600)]}
# 2.
# -> dict = {"classic":650, "pop":600}
# -> dict2 = {"classic":[(0, 650), (2, 150)], "pop":[(1, 600)]}
# 3.
# -> dict = {"classic":1450, "pop":600}
# -> dict2 = {"classic":[(0, 500), (2, 150), (3, 800)], "pop": [(1, 600)]}
# 4.
# -> dict = {"classic":1450, "pop":3100}
# -> dict2 = {"classic":[(0, 500), (2, 150), (3, 800)], "pop":[(1, 600), (4, 2500)]}

# 두 개의 dictonary를 다뤄야 하는 문제라 푸는 도중에 헷갈릴 수 있다
# 중간마다 print 문으로 어디까지 해결을 했는지 점검해보며 다음 단계를 밟아 가는 게 중요하다

def get_melon_best_album(genre_array, play_array):
    # 1. 장르별로 얼마나 총 재생 횟수를 가지고 있는지
    # 2. 장르 내 어느 인덱스에 재생 횟수가 얼마나 되는지

    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {} # {"장르", [(0,횟수)]}
    for i in range(n):
        genre = genre_array[i] # 장르
        play = play_array[i] # 해당 장르내 특정 노래의 재생 횟수

        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play # 장르별 총 재생횟수 합산
            genre_index_play_array_dict[genre].append([i, play]) # 장르 내 각 노래의 재생횟수
        else: # dict 에 아직 없다면
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
    # print(genre_total_play_dict)
    # print(genre_index_play_array_dict)

    # 장르별로 총 재생횟수가 많은 것부터 2개씩 각 노래의 재생횟수가 많은 것부터 수록
    # 장르별 총 재생횟수 기준으로 정렬 먼저
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    # lambda 문법을 통해 어떤 값을 기준으로 정렬을 할지 sorted 함수에 지정해줄 수 있다
    # 여기서는 item 의 1번째 인덱스 기준, 즉 딕셔너리의 1번째 인덱스 값을 기준으로 정렬

    result = []
    for genre, total_play in sorted_genre_play_array:
        # print(genre, total_play)
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)

        # 최대 2곡씩만 넣어야 함
        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            # print("index ", index, "play ", play)
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))