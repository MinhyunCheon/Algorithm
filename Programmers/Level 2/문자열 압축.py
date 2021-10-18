문제 설명
데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.
최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데,
이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다.
"어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다.
다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다.
이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

제한사항
s의 길이는 1 이상 1,000 이하입니다.
s는 알파벳 소문자로만 이루어져 있습니다.



def get_zip_str(s, loop_len):
    # 시작 반복 text를 미리 저장하여 반복 횟수 감소 및 비교
    temp_text = s[0:loop_len]
    loop_cnt = 1
    result = ''
    # len(s) + 1까지 반복해야 마지막 값에 대한 처리 가능
    for idx in range(loop_len, len(s) + 1)[::loop_len]:
        if temp_text == s[idx:idx + loop_len]:
            loop_cnt += 1
        else:
            result += ((str(loop_cnt) if loop_cnt > 1 else '') + temp_text)
            loop_cnt = 1
            temp_text = s[idx:idx + loop_len]
            # temp_text에 내용이 있고, loop_len보다 작은 경우 로직이 종료되므로 결과 값 뒤에 추가
            if temp_text and len(temp_text) < loop_len: result += temp_text
    return result

# s의 길이를 2로 나눈 값부터 문자열의 포함 여부를 체크
def solution(s):
    answer = 0
    s_half_idx = len(s) // 2 + 1
    loop_list = []
    # loop_len = 0
    
    # 가장 긴 반복 text 역순 검색
    # 입출력 예 #5 "xababcdcdababcdcd"와 유사하지만, 반복으로 줄일 수 있는 경우("xabababababa")를 체크하지 못함
    # 위의 이유로 테스트 케이스 28번 실패 원인
    # for idx in range(s_half_idx)[::-1]:
    #     if s.count(s[:idx]) > 1:
    #         loop_len = len(s[:idx])
    #         break
    
            
    # 2, 3, 4, 6, 7, 8, 11, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28 실패
    # if loop_len == 0: answer = len(s)
    # else:
        # zip_loop_len = len(get_zip_str(s, loop_len))
        # # 한 문자가 반복되는 경우 자르는 길이를 1로 수행한 결과와 비교하는 로직 추가(3번 통과)
        # if loop_len > 1 and len(get_zip_str(s, 1)) < zip_loop_len: zip_loop_len = len(get_zip_str(s, 1))
        # answer = zip_loop_len
        
        # 어떤 단위가 정답일지 사전에 확인할 수 있는 방법이 없어 1 ~ s 길이의 절반까지 모두 검사하도록 변경
        # 28번 실패, 우려했던 것과는 달리 심각한 성능저하는 없음
        # 가장 많은 시간이 걸린 21 케이스 테스트 21 〉통과 (4.56ms, 10.3MB)
        # for loop in range(1, s_half_idx): loop_list.append(len(get_zip_str(s, loop)))
        # answer = min(loop_list)
        
    # 가장 긴 반복 text 역순 검색을 제거하고 풀서치하면 28번 통과, 5번 런타임 에러
    for loop in range(1, s_half_idx): loop_list.append(len(get_zip_str(s, loop)))
    answer = min(loop_list) if loop_list else 1 # 테스트 5, s의 길이가 1인 경우
    
    return answer
