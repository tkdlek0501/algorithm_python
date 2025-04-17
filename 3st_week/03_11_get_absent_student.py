# Q. 오늘 수업에 많은 학생들이 참여했습니다.
# 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다.
#
# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때,
# 출석하지 않은 학생의 이름을 반환하시오.

# 아이디어
# 1. 단 한 명의 학생을 찾아야 한다.
# 2. 배열의 형식으로 데이터가 주어진다
# 3. 탐색 해야 할텐데 어떤 방법이 좋을까?
# 총 학생을 dictionary 에 넣고 출석한 학생을 빼기?

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {} # 딕셔너리
    for key in all_array:
        dict[key] = True

    for key in present_array:
        del dict[key] # 딕셔너리의 데이터를 지우는 방법

    for key in dict.keys():
        return key


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))