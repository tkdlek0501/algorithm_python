# Q. 쿼드압축 후 개수세기

# 0과 1로 이루어진 2^n x 2^n 크기의 2차원 정수 배열
# 1. 압축할 특정 영역을 S 라고 정의
# 2. S 내부에 모든 수가 같은 값이면, S를 해당 수 하나로 압축
# 3. 그렇지 않으면, S를 정확히 4개의 균일한 정사각형 영역으로 나누고
# 각 정사각형 영역에 대해 같은 방식의 압축 시도

# 배열에 최종적으로 남은 0의 개수와 1의 개수를 배열에 담아서 return
# arr 행의 개수 1이상 1024 이하
# 2의 거듭 제곱수 형태
# 즉, arr 행의 개수는 1, 2, 4, 8,..., 1024
# arr 각 행의 길이는 arr의 행의 개수와 같다 (정사각형 배열)
# arr 각 행에 있는 모든 값은 0 또는 1

# <풀이>
# 재귀적으로 줄여나가면서 풀면된다 (1024 * 1024 라서 2중 for문 가능 범위)
# 영역의 시작점과 사이즈를 알면 반복해서 풀어나갈 수 있다

def solution(arr):
    result = [0, 0]  # result[0]: 0의 개수, result[1]: 1의 개수

    def compress(x, y, size): # 영역의 시작점과 사이즈
        # 압축 가능 여부 판단
        first = arr[x][y] # 그 영역의 첫번째 값
        all_same = True

        for i in range(x, x + size): # 시작점 x 부터 x + size 까지
            for j in range(y, y + size):
                if arr[i][j] != first: # 다른 값이 존재하면
                    all_same = False
                    break
            if not all_same:
                break

        if all_same: # 모두 같은 값이라면 result에 반영
            result[first] += 1 # 더 이상 분할할 필요없이 result 에 반영
        else:
            new_size = size // 2 # 사이즈를 반으로 줄이며 4개로 나눠서 반복
            compress(x, y, new_size)                       # 좌상
            compress(x, y + new_size, new_size)            # 우상
            compress(x + new_size, y, new_size)            # 좌하
            compress(x + new_size, y + new_size, new_size) # 우하

    compress(0, 0, len(arr)) # 0, 0 부터 + 초기 size는 배열의 길이
    return result

# <피드백>
# 아이디어는 떠오르는데 구현이 바로 안된다
# 우선 모두 값인지 확인하려면 all_same 같은 변수가 필요하긴 하다
# first 값도 알 수 있으니 이것과 비교하면 된다
# 0인지 1인지도 굳이 구분하지 않고 어차피 0 or 1 이니까 first의 값으로 넣어도 된다

# 반복해서 압축하는 문제이기 때문에 분할정복해야 함
# 1024 개가 최대이므로 2중 for문 가능하도 재귀적으로 풀 수 있음
# 아이디어는 계속 4개로 나누는 거니까
# 4개로 나눈 영역의 좌상 좌표를 사이즈와 함께 파라미터로 넘겨주면 됨


