문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.



# from collections import deque
import heapq

def solution(scoville, K):
    answer = 0
    # heapq를 사용해 heap 생성
    h = sorted(scoville)
    is_possible = False
    # 굳이 힙 배열을 만들지 않고 일반 배열로 사용 가능
    # for x in scoville: heapq.heappush(h, x)
    
    # 테스트 16, 마지막 1개의 값이 K이상인 경우, 조건이 1초과 이기 때문에 해당 조건을 검사하지 못해 실패
    while len(h) > 1:
        if h[0] >= K:
            is_possible = True
            break
        # 힙을 활용해 문제를 해결했지만, 힙에 대한 추가적인 이해 필요
        heapq.heappush(h, heapq.heappop(h) + (heapq.heappop(h) * 2))
        answer += 1
        
    # 테스트 16의 조건을 만족하기 위해 h[0] < K 조건 추가
    if h[0] < K and not is_possible: answer = -1
    
    # scoville_list = deque(sorted(scoville))
    # scoville_dict = {}
    # before_lower = 0
    
    # for x in scoville:
    #     if scoville_dict.get(x) is None: scoville_dict[x] = 1
    #     else: scoville_dict[x] += 1

#     is_possible = False
    
#     # 테스트 16 실패, 효율성 전부 실패(deque 선언하고, 일반 list 사용)
#     # deque 사용 시에도 정확성 16번, 효율성 전체 실패(시간 초과)
#     # 조건문 min(scoville_list) -> scoville_list[0] 변경, 효율성 실패
#     while len(scoville_list) >= 2:
#         if scoville_list[0] > K:
#             is_possible = True
#             break
#         scoville_list = sorted(scoville_list)
#         scoville_list.append(scoville_list.pop(0) + (scoville_list.pop(0) * 2))
#         answer += 1
        
    return answer
