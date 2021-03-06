문제 설명
복서 선수들의 몸무게 weights와, 복서 선수들의 전적을 나타내는 head2head가 매개변수로 주어집니다. 복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 하도록 solution 함수를 완성해주세요.

전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.

제한사항
weights의 길이는 2 이상 1,000 이하입니다.
weights의 모든 값은 45 이상 150 이하의 정수입니다.
weights[i] 는 i+1번 복서의 몸무게(kg)를 의미합니다.
head2head의 길이는 weights의 길이와 같습니다.
head2head의 모든 문자열은 길이가 weights의 길이와 동일하며, 'N', 'W', 'L'로 이루어진 문자열입니다.
head2head[i] 는 i+1번 복서의 전적을 의미하며, head2head[i][j]는 i+1번 복서와 j+1번 복서의 매치 결과를 의미합니다.
'N' (None)은 두 복서가 아직 붙어본 적이 없음을 의미합니다.
'W' (Win)는 i+1번 복서가 j+1번 복서를 이겼음을 의미합니다.
'L' (Lose)는 i+1번 복사가 j+1번 복서에게 졌음을 의미합니다.
임의의 i에 대해서 head2head[i][i] 는 항상 'N'입니다. 자기 자신과 싸울 수는 없기 때문입니다.
임의의 i, j에 대해서 head2head[i][j] = 'W' 이면, head2head[j][i] = 'L'입니다.
임의의 i, j에 대해서 head2head[i][j] = 'L' 이면, head2head[j][i] = 'W'입니다.
임의의 i, j에 대해서 head2head[i][j] = 'N' 이면, head2head[j][i] = 'N'입니다.



from operator import itemgetter
def solution(weights, head2head):
    answer = []
    player_list = []
    weights_len = len(weights)
    for index in range(0, weights_len):
        # 승리 횟수
        win_count = head2head[index].count('W')
        temp = {'idx' : index, 'weight' : weights[index], 'win_rate': 0, 'heavy_player_win' : 0}
        
        # 본인보다 높은 몸무게 선수를 이긴 횟수
        match_count = 0
        if win_count > 0:
            for index2 in range(0, weights_len):
                if head2head[index][index2] == 'W':
                    if weights[index] < weights[index2]: temp['heavy_player_win'] += 1
                elif head2head[index][index2] == 'N': continue
                match_count += 1

            # 승률 산정 백분율로는 값이 나오지 않는 경우가 있어 10000배 적용
            temp['win_rate'] = (win_count / match_count) * 10000

        player_list.append(temp)
    player_list = sorted(player_list, key=lambda x:(-x['win_rate'], -x['heavy_player_win'], -x['weight'], x['idx']))
    answer = [x['idx']+1 for x in player_list]
        
    return answer
