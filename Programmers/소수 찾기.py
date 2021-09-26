문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.



import math
def solution(n):
    answer = 1
    prime_list = [2]
    n_sqrt = int(math.sqrt(n))
    target = n
    
    # 소수 구하기
    for x in range(3, n_sqrt + 1):
        prime_flag = True
        for y in range(2, x):
            if x % y == 0:
                prime_flag = False
                break
        if prime_flag:
            prime_list.append(x)
            answer += 1

    while(n_sqrt < target):
        prime_flag = True
        for x in prime_list:
            if target % x == 0:
                prime_flag = False
                break
        if prime_flag: answer += 1
        target -= 1
    
    return answer
