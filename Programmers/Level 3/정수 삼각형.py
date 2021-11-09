def solution(triangle):
    answer = 0
    # triangle_copy = [] + triangle[:]  # 원본 보존을 위해 copy()를 여러 방법으로 수행했지만 값이 동기화됨
    # list 내부에 list 형식으로 선언되어 있어 내부 주소 값을 공유하기 때문에 발생하는 문제

    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            left = triangle[row][col] + triangle[row + 1][col]
            right = triangle[row][col] + triangle[row + 1][col + 1]
            triangle[row][col] = left if left > right else right
            
    answer = triangle[0][0]
            
    # print(id(triangle_copy))
    # print(triangle_copy)
    # print(id(triangle))
    # print(triangle)
    
    # sum_list = [triangle[0]]
    
    # 하향식 요소 4개부터 값이 틀어짐
#     for row in range(1, len(triangle)):
#         temp = []
#         row_len = len(triangle[row])

#         for col in range(pow(2, row_len)):
#             if col != 0:
#                 temp.append(triangle[row][col] + sum_list[row - 1][col - 1])
#             if col != row_len - 1:
#                 temp.append(triangle[row][col] + sum_list[row - 1][col])

#         sum_list.append(temp)
#     print(sum_list)
#     answer = max(sum_list[-1])

    return answer
