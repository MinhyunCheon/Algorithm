문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.



from collections import deque
import itertools

# 숫자의 순서가 바뀔 수 있다는 가정하에 접근했으나, 숫자의 위치는 고정인 것으로 판단
# 많은 경우의 수를 따지기보다 문제에 제시된 스크립트 자체의 구현에 1차적으로 집중
def solution(numbers, target):
    answer = 0
    # 값을 제외하는 경우 +한 값에서도 제외하기 때문에 2배의 값이 차감
    # numbers의 값은 양의 정수만 있기 때문에 절대 값으로 수치 비교 -> 제한사항에 1이상 1000이하로 명시
    short_val = (sum(numbers) - target) // 2
    numbers_len = len(numbers)
    
    # 파이썬의 기능이 너무 쉽게 구현되어 있어 추가 정리 필요
    answer_list = [x for idx in range(1, numbers_len) for x in itertools.combinations(numbers, idx) if sum(x) == short_val]
    answer = len(answer_list)
    
    # 최초 로직, 라이브러리를 사용하지 않고 접근
    # queue = deque()
    
#     pivot_idx = 0
#     while pivot_idx < numbers_len:
#         is_answer = False
#         # if numbers[pivot_idx] == short_val: is_answer = True # 현재 값이 short_val과 일치하는 경우
        
#         if is_answer: answer += 1
#         pivot_idx += 1
        
    return answer
