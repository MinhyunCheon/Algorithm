문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000



def solution(left, right):
    answer = 0

    # 마지막 값을 포함해야 하므로 right + 1
    for x in range(left, right + 1):
        divisor_cnt = 0
        
        # x / 2 지점까지만 탐색하면, 모든 약수에 대한 경우 검사
        for y in range(1, (x // 2) + 1):
            if x % y == 0: divisor_cnt += 1
        
        # 자기 자신이 약수에 포함되므로 + 1
        divisor_cnt += 1
        if divisor_cnt % 2 == 0: answer += x
        else: answer -= x
    
    return answer
