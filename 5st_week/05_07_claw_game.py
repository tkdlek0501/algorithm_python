# 게임개발자인 "죠르디"는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
# "죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

# 게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이며
# 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 "5 x 5" 크기의 예시입니다).
# 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다.
# 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다.
# 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다.
# 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다.
# 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.

# 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다.
# 위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 두 개가 없어집니다.

# 크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
# 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다.
# (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)
#
# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
# 0은 빈 칸을 나타냅니다.
# 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
# moves 배열의 크기는 1 이상 1,000 이하입니다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

# 입출력 예
# board	moves	result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

# Q. 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# 4 가 출력되어야 합니다.


# <문제분석>
# 1 x 1 크기의 칸들로 이루어진
# N x N 정사각 격자
# 위쪽에는 크레인이 있고, 오른쪽에는 또다른 바구니가 있다
# 격자의 가장 아래 칸부터 차곡차곡 쌓여있다
# 크레인의 움직임 : 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 올릴 수 있고
# 이 이현은 바구니에 쌓이게 되는데 이 때도 가장 아래 칸부터 순서대로 쌓인다
# 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 된다
# 크레인 작동시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳이라면 아무런 일도 일어나지 않는다
# 입력)
# 1. 격자의 상태가 담긴 2차원 배열 board
# 2. 크레인을 작동시킨 위치가 담긴 배열 moves

# 출력)
# 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return

# <문제풀이>
# 인형은 1 ~ 100 까지 100가지 종류의 인형이 있다
# moves 는 1 부터 시작한다
# 바구니에 연속으로 같은 애가 2개이면 터트려야 하고 이를 터트린 개수에 저장해서 결과로 반환해야 한다
# 바구니는 선입후출 이므로 stack 으로 관리
# 터뜨린 개수 관리

# <구현>
# moves 를 순회하면서
# moves - 1 이 col 인덱스
# row 인덱스는 그 col 의 가장 위에 있는 값이어야 한다
# 따라서 이것도 0이 아닌 값이 나올 때 까지 순회 필요
# peek 해서 같으면 pop 하면서 result에 2개 저장
# peek 해서 다르면 push

# <내 풀이>
def solution1(board, moves):
    answer = 0

    max_row = len(board) # 세로 최대 길이
    # print("max_row : ", max_row)

    bucket = [] # 바구니 stack

    for i in moves: # 매 동작
        # print("basket : ", basket)
        col_index = i - 1 # col 인덱스
        for row_index in range(max_row): # 그 때 뽑히는 게 있는지
            doll = board[row_index][col_index]
            # print("doll : ", doll)
            if doll != 0: # 인형이 뽑혔다면
                if bucket: # 바구니에 인형이 있다면
                    if doll == bucket[-1]: # 맨 마지막 인형 봐서 같은 인형이면
                        # print("터트림 : ", basket[-1], doll)
                        bucket.pop() # 꺼내고
                        answer += 2 # 2개 터트려짐
                    else: # 같은 인형 아니면
                        bucket.append(doll)
                else: # 바구니에 인형 없으면
                    bucket.append(doll)
                board[row_index][col_index] = 0 # 바구니로 옮겨갔으니까 격자에서 0으로 만들어준다
                break # 맨 위 인형 뽑았으니까 다음 동작으로 넘어간다

    return answer

def solution(board, moves):
        bucket = []
        answer = 0

        for move in moves:
            index = move - 1
            for row_info in board:
                if row_info[index] != 0: # 인형이면
                    bucket.append(row_info[index])
                    row_info[index] = 0
                    if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                        answer += 2
                        bucket = bucket[0:-2]
                    break
        return answer

print(solution(board, moves))