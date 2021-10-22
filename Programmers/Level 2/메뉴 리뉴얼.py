문제 설명
레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다.
어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.

예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
(각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)

손님 번호	주문한 단품메뉴 조합
1번 손님	A, B, C, F, G
2번 손님	A, C
3번 손님	C, D, E
4번 손님	A, C, D, E
5번 손님	B, C, F, G
6번 손님	A, C, D, E, H
가장 많이 함께 주문된 단품메뉴 조합에 따라 "스카피"가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.

코스 종류	메뉴 구성	설명
요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.

[문제]
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때,
"스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

[제한사항]
orders 배열의 크기는 2 이상 20 이하입니다.
orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
각 문자열은 알파벳 대문자로만 이루어져 있습니다.
각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
course 배열의 크기는 1 이상 10 이하입니다.
course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
course 배열에는 같은 값이 중복해서 들어있지 않습니다.
정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.



from itertools import combinations

def get_orders_by_course(order, course):
    return list(map(''.join, combinations(order, course)))

def solution(orders, course):
    answer = []

    # 사실상 같은 값이지만, 순서의 차이로 확인하지 못하는 케이스 발생(입출력 예 3, XW - WX)
    for c in course:
        course_dict = {}
        temp_list = []
        max_cour = 0
        
        # 배열 + 연산을 통해 order 별 나올 수 있는 경우의 수를 하나의 배열로 저장
        for x in orders: temp_list += get_orders_by_course(x, c)
        # dict를 통해 요소별 횟수 저장
        for x in temp_list:
            # x를 검사하기 전, 정렬을 통해 오름차순으로 통일
            sort_x = ''.join(sorted(x))
            if course_dict.get(sort_x) is None: course_dict[sort_x] = 1
            else: course_dict[sort_x] += 1
                
        # 결과를 내림차순한 첫번째 값으로 최대값 설정
        temp_list = sorted(course_dict.items(), key = lambda x : -x[1])
        if temp_list: max_cour = temp_list[0][1]

        # 내림차순 정렬하여 얻은 최대 값이 2이상이 아닌 경우 단건 주문이므로 조건에 부합하지 않아 무시
        if max_cour >= 2:
            # 최대값과 같은 값을 answer에 추가
            for x in temp_list:
                if max_cour == x[1]: answer.append(x[0])
                else: break
       
    # 최종 결과 오름차순 정렬
    answer = sorted(answer)
    
    # order_set = set()
    # course_list = []
    
    # append가 아닌 +가 원하는 값을 얻을 수 있음
    # print(['a','v'] + ['b','a'])
    
    # print(course_list)
        
    # while True:
        # for x in course_lis
        
    # for x in course_list:
    #     course_dict = {}
    #     for y in x:
    #         print(y)
            
            
    # print(course_list[0])
    
    # 3중 반복문 지양
    # for x in orders:
    #     for y in get_orders_by_course(x, 2):
    #         if course_dict.get(y) is None: course_dict[y] = 1
    #         else: course_dict[y] += 1
    
    # 주문들을 종합한 뒤 중복을 제거하여 유일한 메뉴 생성
    # for x in orders: order_set.update(x)
    
    # course 별 조합 가능한 메뉴 생성
    # for x in course: course_list.append(list(map(''.join, combinations(order_set, x))))
    
    return answer
