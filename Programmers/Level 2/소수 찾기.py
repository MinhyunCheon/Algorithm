문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.



import itertools as it
import math

# 소수 체크, 소수인 경우 1을 반환
def prime_check(num):
    is_prime = True
    # range()는 sqrt_num 미만의 값을 검색하므로 +1하여 자기 자신도 검사
    # Test Case 2, 10, 11, 12
    sqrt_num = int(math.sqrt(num)) + 1
    
    for x in range(2, sqrt_num):
        if num % x == 0:
            is_prime = False
            break
            
    return 1 if is_prime else 0

def solution(numbers):
    answer = 0
    numbers_len = len(numbers) + 1
    num_tuple = []
    num_list = []
    
    # 순열의 개념에 대한 추가 정리 필요
    for x in range(1, numbers_len): num_tuple.append(list(it.permutations(numbers, x)))
    # 튜플로 나눠 저장된 값을 하나의 값으로 저장
    for x in num_tuple:
        for y in x:
            temp = int(''.join(y))
            # int로 변환하여 0으로 시작하는 값 처리
            # 중복된 값은 저장하지 않음
            # 0과 1은 소수가 될 수 없기 때문에 1이상인 값만 저장
            if not temp in num_list and temp > 1: num_list.append(temp)
    
    # prime_check 함수를 통해 소수 체크
    for x in num_list: answer += prime_check(x)
        
    return answer
