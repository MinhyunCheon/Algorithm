문제 설명
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라	10진법	124 나라
1	1	6	14
2	2	7	21
3	4	8	22
4	11	9	24
5	12	10	41
자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
n은 500,000,000이하의 자연수 입니다.



# 3으로 나눈 나머지와 몫으로 구분하여 계산 -> 다수 케이스 실패
# 3진법으로 변환 후, 3 -> 4로 치환 -> 3의 배수 몫에서 문제 발생
def solution(n):
    answer = ''
    
    share = n
    balance = n
    stack = []
    
    while share > 0:
        balance = share % 3
        share //= 3
        if balance % 3 == 0:
            stack.append('4')
            share -= 1 # 3을 4로 치환한 뒤 몫을 -1 해줘야 의도한 값을 구할 수 있음
        else: stack.append(str(balance))
            
    answer = ''.join([x for x in stack[::-1]])
    
#     # num_list = [1, 2, 4] # -1 등 원하지 않는 값이 나오는 경우가 있어 dict로 변경
#     num_dict = {1 : '1', 2 : '2', 3 : '4'}
#     share = n
#     balance = n
    
#     # 3이하의 값은 연산할 필요없이 값 리턴
#     if n <= 3: return str(num_dict[n])
#     while share >= 2:
        
#         balance = share % 3 # 나머지를 우선 계산해야 정확한 값을 얻을 수 있음
#         share //= 3
#         print(f'share: {share}, balance: {balance}')
        
#         # 나머지가 0인 경우를 처리하지 않으면 런타임 에러 발생
#         # if balance >= 0: answer += (str(num_dict[balance + 1]))
        
#     # answer += str(num_dict[share + 1])
    
    return answer
