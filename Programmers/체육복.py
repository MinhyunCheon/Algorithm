문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.

# 초기에 해당 조건을 고려하지 않아 사이드 이펙트 발생
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.



# 값을 비교하며 로직을 진행하는 것보다 최대한 정제된 데이터를 비교하는 것이 효율성이나 결과에 도움이 되는 것으로 판단
# 차후 수정 및 사이드 이펙트 최소화를 위해 제한사항을 하나씩 처리하는게 아닌 전체적인 제한사항을 고려한 로직 구현의 필요성을 느낌
# def reserve_task(lost_one, lost_list, reserve_one, reserve_list):
def reserve_task(reserve_one, reserve_list):
    # lost_list.remove(lost_one)    # 분실자 목록의 정보를 갱신해도 해당 문제에서 활용되지 않으므로 제거
    reserve_list.remove(reserve_one)
    return 1

# 값을 비교하며 로직을 진행하는 것보다 최대한 정제된 데이터를 비교하는 것이 효율성이나 결과에 도움이 되는 것으로 판단
# 차후 수정 및 사이드 이펙트 최소화를 위해 제한사항을 하나씩 처리하는게 아닌 전체적인 제한사항을 고려한 로직 구현의 필요성을 느낌
# def reserve_task(lost_one, lost_list, reserve_one, reserve_list):
def reserve_task(reserve_one, reserve_list):
    # lost_list.remove(lost_one)    # 분실자 목록의 정보를 갱신해도 해당 문제에서 활용되지 않으므로 제거
    reserve_list.remove(reserve_one)
    return 1

def solution(n, lost, reserve):
    # answer = n - len(lost)
    # lost_copy = lost.copy()   # 파이썬은 call by reference가 기본값
    # reserve_copy = reserve.copy()   # 코드 상 참조하지 않지만 원본 데이터 보존을 위해 선언
    
    lost_list = list(set(lost) - set(reserve))  # 
    reserve_list = list(set(reserve) - set(lost))
    answer = n - len(lost_list)
    
    # 값을 비교하며 로직을 진행하는 것보다 최대한 정제된 데이터를 비교하는 것이 효율성이나 결과에 도움이 되는 것으로 판단
    # 3, 7, 12 테스트 케이스를 통과하지 못함, 추후 확인 필요
    # if 1 in lost_copy:
    #     # if 1 in reserve_copy: answer += reserve_task(1, lost_copy, 1, reserve_copy) # 여별을 가진 학생이 도난당한 경우
    #     if 2 in reserve_copy: answer += reserve_task(1, lost_copy, 2, reserve_copy)        
    # if n in lost_copy:
    # #     if n in reserve_copy: answer += reserve_task(n, lost_copy, n, reserve_copy)
    #     if (n - 1) in reserve_copy: answer += reserve_task(n, lost_copy, (n - 1), reserve_copy)
            
    # lost_copy_2 = lost_copy.copy()   # 앞뒤가 제거된 최종 리스트를 저장
        
    for x in lost_list:    # 리스트에 변형이 생기는 경우 반복문이 의도대로 작동하지 않음
        # if x in reserve:
        #     reserve_task(x, lost_copy, x, reserve_copy)
        #     continue
            
        temp_reserve = x
        if (x - 1) in reserve_list: temp_reserve -= 1
        elif (x + 1) in reserve_list: temp_reserve += 1
        
        if temp_reserve != x: answer += reserve_task(temp_reserve, reserve_list)
    
    return answer
