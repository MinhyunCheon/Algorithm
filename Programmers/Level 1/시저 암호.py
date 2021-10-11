문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.



# 대문자 알파벳 아스키 값 65 ~ 90
# 소문자 알파벳 아스키 값 97 ~ 122
# 공백은 메인 로직에서 필터
def convert(str, shift_index):
    ord_str = ord(str)
    is_upper = True
    first_index = 65
    last_index = 90
    shift_ord = ord_str + shift_index
    
    # if ord_str >= 65 and ord_str <= 95: pass
    # elif ord_str >= 97 and ord_str <= 122: pass
    
    if ord_str > 90:
        is_upper = False
        first_index = 97
        last_index = 122
        
    if shift_ord > last_index: return chr(first_index + (shift_ord - last_index - 1))   # 처음 값으로 이동할 때 1소모
    
    return chr(shift_ord)

def solution(s, n):
    answer = ''
    s_list = list(s)
    
    for x in s_list:
        # print(chr(ord(x) + n))    # 알파벳 이외의 값이 출력될 수 있음
        if x == ' ':
            answer += ' '
            continue
        answer += convert(x, n)
        
    return answer
