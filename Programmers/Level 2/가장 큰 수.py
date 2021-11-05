문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.



# from itertools import combinations    # 순서가 다른 같은 요소는 반환하지 않음
# from itertools import permutations
import functools

def compare(n1, n2):
    str_n1 = str(n1)
    str_n2 = str(n2)
    return 1 if int(str_n1 + str_n2) < int(str_n2 + str_n1) else -1

def solution(numbers):
    answer = ''
    
    for x in sorted(numbers, key = functools.cmp_to_key(compare)):
        answer += str(x)
    
    # 11번, 모든 요소가 0인 경우 처리
    if answer.startswith('0'): answer = '0'

#     # 버블소트 활용, 1, 2, 3, 5, 6 시간초과
#     for y in range(len(numbers) - 1, 0, -1):
#         for x in range(0, y):        
#             if int(str(numbers[x]) + str(numbers[x+1])) > int(str(numbers[x+1]) + str(numbers[x])):
#                 temp = numbers[x+1]
#                 numbers[x+1] = numbers[x]
#                 numbers[x] = temp
            
#     for x in numbers[::-1]: answer += str(x)



#     numbers_len = len(str(max(numbers)))
#     numbers_dict = {}
    
#     # 11, 12, 14, 15 실패
#     for x in numbers:
#         str_x = str(x)
#         loop_cnt = numbers_len - len(str_x)
#         # [str_x + (str_x * loop_cnt), 1] -> 12, 14, 15 실패
#         # [str_x + (str_x[-1] * loop_cnt), 1] -> 1 ~ 6 실패, 7 ~ 15 통과
#         if numbers_dict.get(str_x) is None: numbers_dict[str_x] = [str_x + (str_x[-1] * (loop_cnt)), 1]
#         else: numbers_dict[str_x][1] += 1   # 같은 숫자가 존재하는 경우 처리

#     for x in sorted(numbers_dict.items(), key = lambda x : (x[1], -int(x[0])), reverse = True):
#         answer += (x[0] * (x[1][1]))
    
#     # 11번, 모든 요소가 0인 경우 처리
#     if answer.startswith('0'): answer = '0'
    # 1 ~ 11, 시간초과    
#     temp = []
    
#     for x in list(permutations(numbers, len(numbers))):
#         temp.append(int(str(x).replace(', ', '')[1:-1]))
        
#     answer = str(max(temp))
    
    return answer
