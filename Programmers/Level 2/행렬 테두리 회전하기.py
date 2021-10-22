문제 설명
rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다.
이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
다음은 6 x 6 크기 행렬의 예시입니다.

행렬 테두리 회전하기_1.png

이 행렬에 (2, 2, 5, 4) 회전을 적용하면, 아래 그림과 같이 2행 2열부터 5행 4열까지 영역의 테두리가 시계방향으로 회전합니다. 이때, 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의하세요.

행렬 테두리 회전하기_2.png

행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때,
각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.



from collections import deque

def solution(rows, columns, queries):
    answer = []
    arr = []
    
    # 주어진 크기의 배열 선언과 값 정의
    # add_val = (y * rows) + 1은 정사각형일 때만 유효 
    for y in range(rows):
        temp = []
        add_val = (y * columns) + 1
        for x in range(columns):
            # 연산을 줄이기 위해 상위 레벨 고정 값을 add_val로 분리
            # temp.append((y * rows) + x + 1)
            temp.append(add_val + x)
        arr.append(temp)
    # print(arr)
    
    # 주어진 queries 탐색
    # 예제는 x가 행, y가 열을 의미하여 일반적인 개념과 다름
    # 3중 반복문은 좋은 방식이 아니라고 판단
    for q in queries:
        # loop_cnt = 0
        x1 = q[1] - 1
        y1 = q[0] - 1
        x2 = q[3] - 1
        y2 = q[2] - 1
        queue = deque()
        
        # 테스트 3 ~ 11 실패
        # 이동할 대상 값들 저장
        for x in range(x1, x2 + 1): queue.append(arr[y1][x])
        for y in range(y1 + 1, y2 + 1): queue.append(arr[y][x2])
        for x in range(x2 - 1, x1 - 1, -1): queue.append(arr[y2][x])
        for y in range(y2 - 1, y1, -1): queue.append(arr[y][x1])
        answer.append(min(queue))
        
        arr[y1][x1] = queue.pop()
        for x in range(x1 + 1, x2 + 1): arr[y1][x] = queue.popleft()
        for y in range(y1 + 1, y2 + 1): arr[y][x2] = queue.popleft()
        for x in range(x2 - 1, x1 - 1, -1): arr[y2][x] = queue.popleft()
        for y in range(y2 - 1, y1, -1): arr[y][x1] = queue.popleft()
        
        # temp = 0 # 끝자리에 위치한 값 임시 저장
        # temp2 = 0
        
#         # 직사각형 윗변
#         # 좌측부터 수행하면 값을 보장할 수 없으므로 우측부터 당기는 방식 선택
#         temp = arr[y1 + 1][x2]
#         arr[y1 + 1][x2] = arr[y1][x2]
#         for x in range(x1, x2 + 1)[::-1]: arr[y1][x] = arr[y1][x - 1]
            
#         # 직사각형 우측변
#         temp2 = arr[y2][x2 - 1]
#         print(temp2)
        
        # print(f'{x1} {y1} {x2} {y2}')
#         while loop_cnt < 4:
#             # print(arr[x1][y1])
#             if loop_cnt == 0:
#                 if x1 == x2:
#                     loop_cnt += 1
#                     continue
#                 x1 += 1
#             elif loop_cnt == 1:
#                 if y1 == y2:
#                     loop_cnt += 1
#                     break
#                 y += 1
            
#             if loop_cnt == 3: break
    return answer
