문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.



def solution(arr1, arr2):
    answer = []
    
    for row in range(len(arr1)):
        temp = []
        
        for x in range(len(arr2[0])):
            temp_num = 0
            
            for y in range(len(arr2)): temp_num += arr1[row][y] * arr2[y][x]

            temp.append(temp_num)
        
        answer.append(temp)
    
    return answer
