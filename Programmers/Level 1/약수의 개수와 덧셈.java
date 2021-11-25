문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서,
약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000



class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        for(int leftIdx = left; leftIdx <= right; leftIdx++) {
            int divisorCnt = 1; // 1과 자기 자신은 항상 약수이므로 2로 시작
            int halfLeft = leftIdx / 2;
            int tempLeft = 0;
            
            for(int num = 1; num <= halfLeft; num++) {
                if(leftIdx % num == 0) divisorCnt++;
            }
            
            tempLeft = leftIdx;
            if(divisorCnt % 2 != 0) tempLeft *= -1;
            answer += tempLeft;
        }
        
        return answer;
    }
}
