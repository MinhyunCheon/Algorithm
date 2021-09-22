문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.



def solution(n, m):
    answer = []
    gcd = get_gcd(sorted([n, m]))
    answer.append(gcd)
    answer.append(n * m / gcd)

    return answer

def get_gcd(num_list):
    num_a = num_list[1]
    num_b = num_list[0]
    
    while(True):
        if num_a % num_b == 0: return num_b

        temp = num_b
        num_b = num_a % num_b
        num_a = temp
