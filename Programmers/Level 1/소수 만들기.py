문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.



import math

def solution(nums):
    answer = 0
    sum_list = []
    last_idx = len(nums)
    idx1 = 0
    idx2 = 1
    idx3 = 2
    
    # 3개의 숫자를 뽑는 경우를 모두 탐색해 합 저장
    while True:
        sum_list.append(nums[idx1] + nums[idx2] + nums[idx3])
        idx3 += 1
        
        if idx3 == last_idx:
            idx2 += 1
            if idx2 == last_idx - 1:
                idx1 += 1
                if idx1 == last_idx - 2: break
                idx2 = idx1 + 1
            idx3 = idx2 + 1
            
    # 소수 체크
    for x in sum_list:
        prime_flag = True
        n_sqrt = int(math.sqrt(x)) + 1
        for y in range(2, n_sqrt):
            if x % y == 0:
                prime_flag = False
                break
        if prime_flag: answer += 1

    return answer
