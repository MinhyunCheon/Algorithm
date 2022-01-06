문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.



class Solution {
    public int solution(int n) {
        int answer = n;
        int halfN = n / 2;
        
        for(int idx = 1; idx <= halfN; idx++) {
            if(n % idx == 0) answer += idx;
        }
        
        return answer;
    }
}
