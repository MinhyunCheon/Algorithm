문제 설명
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

[제한사항]
numbers 배열의 크기는 1 이상 1,000 이하입니다.
numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
hand는 "left" 또는 "right" 입니다.
"left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.



# 초기 손가락의 위치는 왼쪽 *, 오른쪽 #
# numbers에는 누를 숫자의 위치, hand는 주로 사용하는 손의 정보
# 손가락은 상하좌우로만 이동 가능, 이미 다음 숫자 위치에 있는 경우까지 포함 1 cost에 5가지 경우에 대응
# 1, 4, 7은 무조건 왼손, 3, 6, 9는 오른손 사용
# 중간에 위치한 2, 5, 8, 0의 경우 두 손가락 중 가까운 위치의 손가락을 판단해 사용
# 두 손가락의 cost가 같다면 주로 사용하는 손가락을 사용
def get_cost(hand_idx, now_idx):
    return abs(hand_idx[0] - now_idx[0]) + abs(hand_idx[1] - now_idx[1])

def solution(numbers, hand):
    answer = ''
    l_idx = '*'
    r_idx = '#'
    # in을 활용하기 위해 문자열로 선언
    l_pad = '147'
    r_pad = '369'
    # 키패드의 정보가 따로 주어지지 않기 때문에 dict로 키패드 인덱스 정보를 저장해 참조
    keypad_dict = {'*': [3, 0], '0': [3, 1], '#': [3, 2]}
    x_idx = 0
    # 1 ~ 9 키패드 정보 저장 로직
    for x in range(1, 10):
        is_last = (x % 3 == 0) # 3의 배수인 경우 같은 행의 키패드 마지막으로 판단
        keypad_dict[str(x)] = [x_idx, 2 if is_last else (x % 3 - 1)]
        if is_last: x_idx += 1

    for x in numbers:
        str_x = str(x)
        use_hand = ''
        if str_x in l_pad: use_hand = 'L'
        elif str_x in r_pad: use_hand = 'R'
        else:
            l_cost = get_cost(keypad_dict[l_idx], keypad_dict[str_x])
            r_cost = get_cost(keypad_dict[r_idx], keypad_dict[str_x])

            if l_cost < r_cost: use_hand = 'L'
            elif r_cost < l_cost: use_hand = 'R'
            else: use_hand = 'L' if hand == 'left' else 'R'
                
        answer += use_hand
        if use_hand == 'L': l_idx = str_x
        else: r_idx = str_x
    
    return answer
