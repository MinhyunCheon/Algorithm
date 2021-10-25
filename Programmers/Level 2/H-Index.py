문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.



# 문제 설명에 대한 이해가 100%인 문제
def solution(citations):
    answer = 0
    sort_citations = sorted(citations, reverse = True)
    idx = 1
    is_allover = True
    
    # 내림차순 정렬 뒤, 인용 횟수가 idx보다 작아지는 시점의 바로 전 idx를 정답으로 입력
    # 모든 요소가 idx보다 큰 경우를 판단하지 못함(테스트 9)
    for x in sort_citations:
        if x < idx:
            answer = idx - 1
            is_allover = False
            break
        idx += 1
    
    # 테스트 9 대응
    if is_allover: answer = len(citations)
        
    return answer
