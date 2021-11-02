문제 설명
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만
1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.



# 2021-11-02, 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다. -> 지문을 꼼꼼히 읽지 않아 해당 조건을 보지 못함

# 최대한 많은 사람을 구출하는 것이 개수를 줄이는 방법이라 판단되므로, 오름차순 정렬 후 진행
# deque import 없이 내림차순 정렬 후, pop()을 통해 진행
# ---------- 테스트 케이스는 통과하지만 실제 제출 시, 다수 오답

from collections import deque

def solution(people, limit):
    answer = 0
    sort_people = deque(sorted(people, reverse = True))

    # 2021-11-02, 초기 구현 시, limit를 꽉 채우는 방식으로 방향을 잡아 복잡도 증가
    while sort_people:
        boat_in = sort_people.popleft()
        if sort_people and boat_in + sort_people[-1] <= limit:
            sort_people.pop()
        answer += 1
        
    # 2021-11-02, 정확성 1, 3, 4, 5, 6, 9, 10, 11, 12, 13 / 효율성 1, 2, 3 런타임 에러
#     while sort_people:
#         boat_in = sort_people.popleft()
        
#         if sort_people and boat_in + 40 <= limit:
#             margin = limit - boat_in
#             temp_x = 0  # for문 내부에서 sort_people의 데이터를 조작하면 오류 발생
#             for x in sort_people:
#                 if x <= margin:
#                     temp_x = x
#                     break
#             # 2021-11-02, temp_x가 0일 때를 제거, 효율성 1, 3 실패
#             if temp_x != 0: sort_people.remove(temp_x)
                    
#         answer += 1
        
#         # 2021-11-02, 효윻성 1, 3 실패
#         if boat_in <= (limit // 2):
#             answer += len(sort_people) // 2
#             if len(sort_people) % 2 == 1: answer += 1
#             break
        
#     boat = []
    
#     while sort_people:
#         boat_in = [] # 보트 탑승 인원을 체크하기 위한 배열

#         # 제한사항에 사람의 몸무게 최소 값은 40이므로 40 미만은 생략
#         if limit - sum(boat_in) >= 40:
#             # 추가 인원이 있는 경우 동승할 수 있는지 체크하여, 가능한 경우 boat_in에 추가
#             for x in sort_people:
#                 if sum(boat_in) + x <= limit:
#                     boat_in.append(x)

#         for x in boat_in: sort_people.remove(x)
#         answer += 1
        
    # people_list = sorted(people, reverse = True)
    # people_len = len(people_list)
    # weight_dict = {}
    # waiting_cnt = people_len
    # now_weight = 0
    # is_margin = True

    # 정확성 1, 4, 5, 효율성 전부 시간초과
#     while True:
#         for x in range(people_len):
#             if people_list[x] != 0 and now_weight + people_list[x] <= limit:
#                 now_weight += people_list[x]
#                 people_list[x] = 0
#                 waiting_cnt -= 1
#             if limit - now_weight < 40: break
                
#         answer += 1
#         now_weight = 0
                
#         if waiting_cnt == 0:
#             if now_weight > 0: answer += 1
#             break

    # pop()과 같이 값을 제거하면 메모리가 소모되기 때문에 dict를 통해 count 비교
    # for x in people_list:
    #     # 제한사항에 각 사람의 최소 몸무게는 40kg이상 조건에 따라 limit - x가 40미만인 경우 무조건 1대의 구명보트를 사용하므로 answer 값 증가 후 저장 생략
    #     if limit - x < 40:
    #         answer += 1
    #         continue
    #     if weight_dict.get(x) is None: weight_dict[x] = 1
    #     else: weight_dict[x] += 1
    #     waiting_cnt += 1
            
    # print(weight_dict)
    
    
    # print(waiting_cnt)
    # 시간 초과 다수
#     while waiting_cnt > 0:
#         for x in weight_dict:
#             if weight_dict[x] > 0 and now_weight + x <= limit:
#                 now_weight += x
#                 weight_dict[x] -= 1
#                 waiting_cnt -= 1
                
#             if limit - now_weight < 40:
#                 is_margin = False
#                 break

#         if not is_margin or waiting_cnt == 0:
#             answer += 1
#             now_weight = 0
#             is_margin = True

    # answer += 1


    # 정확성 1, 4, 5, 효율성 1, 2, 3 오답
#     for idx1 in range(people_len):
#         p1 = people_list[idx1]
        
#         if weight_dict[p1] == 0: continue
#         now_weight += p1
#         weight_dict[p1] -= 1
        
#         for idx2 in range(idx1 + 1, people_len):
#             p2 = people_list[idx2]
            
#             if weight_dict[p2] == 0: continue
#             if now_weight + p2 <= limit:
#                 now_weight += p2
#                 weight_dict[p2] -= 1
#             if limit - now_weight < 40: break
#         answer += 1
#         now_weight = 0

    return answer
