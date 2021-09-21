문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
입출력 예



def solution(arr1, arr2):
    answer = []
    
    x_len = len(arr1[0])
    y_len = len(arr1)
    
    for y in range(0, y_len):
        temp = []
        for x in range(0, x_len):
            temp.append(arr1[y][x] + arr2[y][x])
        answer.append(temp)
    
    return answer
