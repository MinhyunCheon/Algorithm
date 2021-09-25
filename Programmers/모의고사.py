문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.



def solution(answers):
    answer = []
    
    u1 = [1, 2, 3, 4, 5]
    u2 = [2, 1, 2, 3, 2, 4, 2, 5]
    u3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    u1_len = len(u1)
    u2_len = len(u2)
    u3_len = len(u3)
    u1_index = 0
    u2_index = 0
    u3_index = 0
    score_dict = {'1' : 0, '2' : 0, '3' : 0}
    max_score = 0
    
    for x in answers:
        if u1[u1_index] == x:
            score_dict['1'] += 1
        if u2[u2_index] == x:
            score_dict['2'] += 1
        if u3[u3_index] == x:
            score_dict['3'] += 1
        
        
        u1_index += 1
        u2_index += 1
        u3_index += 1
        if u1_index == u1_len: u1_index = 0
        if u2_index == u2_len: u2_index = 0
        if u3_index == u3_len: u3_index = 0
        
    for key, value in score_dict.items():
        if max_score < value: max_score = value
            
    for key, value in score_dict.items():
        if max_score == value: answer.append(int(key))
    
    return answer
