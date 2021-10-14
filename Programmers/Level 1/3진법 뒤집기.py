문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.



def solution(n):
    answer = 0
    share = n
    balance = 0
    result_str = ''
    
    # 3진수로 변환
    while share > 0:
        result_str += str(share % 3)
        share //= 3
    
    # 이미 반전된 상태이므로 다시 3진법으로 변환하면 정답
    answer = int(result_str, 3)
    
    return answer
