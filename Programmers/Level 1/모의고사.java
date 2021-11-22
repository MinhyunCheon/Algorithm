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



import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] a1 = {1, 2, 3, 4, 5};
        int[] a2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] a3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int max_score = 0;
        int len = answers.length;
        int answerLen = 0;
        Map<Integer, Integer> map = new HashMap<> ();
        List<Integer> personList;
        List<Integer> answerList;

        for(int index = 0; index < len; index++) {
            if(answers[index] == a1[index % 5]) map.put(1, (map.get(1) == null ? 0 : map.get(1)) + 1);
            if(answers[index] == a2[index % 8]) map.put(2, (map.get(2) == null ? 0 : map.get(2)) + 1);
            if(answers[index] == a3[index % 10]) map.put(3, (map.get(3) == null ? 0 : map.get(3)) + 1);
        }
        
        personList = new ArrayList<>(map.keySet());
        personList.sort((a, b) -> (map.get(b) - map.get(a)));
        
        max_score = map.get(personList.get(0));
        answerList = new ArrayList<>();
        
        for(Integer i : personList) {
            if(map.get(i) == max_score) answerList.add(i);
            else break;
        }
        
        answerLen = answerList.size();
        answer = new int[answerLen];
        
        for(int idx = 0; idx < answerLen; idx++) {
            answer[idx] = answerList.get(idx);
        }
        
        return answer;
    }
}
