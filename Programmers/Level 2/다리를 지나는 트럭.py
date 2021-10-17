문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다.
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.



# 다리 허용 무게 초과로 추가 트럭이 진입할 수 없는 경우 메인 반복문을 멈추고 스택 첫번째 트럭의 통과까지 한번에 연산하도록 개선 필요
def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing = []   # 이동 중인 트럭 저장
    waiting = truck_weights.copy()  # 원본 보존을 위해 대기 중인 트럭 복사 저장
    crossing_weight = 0 # 현재 이동 중인 트럭의 무게

    while(True):
        for x in crossing:  # 이동 중인 모든 트럭의 소요 시간 1 증가
            x[list(x.keys())[0]] += 1
            
        # 이동 중인 트럭이 있고, 첫번째 트럭 값이 다리 길이에 도달한 경우 조건 실행
        if len(crossing) > 0 and list(crossing[0].values())[0] >= bridge_length:
            # 마지막 이동 트럭인 경우 종료
            if len(crossing) <= 1 and len(waiting) <= 0:
                answer += 1 # 가독성을 위해 위치 변경
                break
            crossing_weight -= list(crossing.pop(0).keys())[0]
            
        if len(waiting) > 0 and weight >= (crossing_weight + waiting[0]):
            crossing.append({waiting[0] : 0})
            crossing_weight += waiting.pop(0)
        answer += 1
    # answer += 1 # 반복문에서 마지막 이동 카운트를 하지 않아 추가 연산
    
    return answer
