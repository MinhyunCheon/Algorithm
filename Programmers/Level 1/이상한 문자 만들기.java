문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.



class Solution {
    public String solution(String s) {
        String answer = "";
        String[] sArr = s.toLowerCase().split(" ", -1); // 두번째 인자로 -1을 줘야 후미에 연속된 공백 처리 가능
        int sArrLen = sArr.length;
        int loopCnt = 1;
        
        String tempStr = "";
        int tempLen = 0;
        
        for(String ss : sArr) {
            tempLen = ss.length();
            
            for(int idx = 0; idx < tempLen; idx++) {
                tempStr = Character.toString(ss.charAt(idx));
                if(idx % 2 == 0) tempStr = tempStr.toUpperCase();
                answer += tempStr;
            }
            
            if(loopCnt < sArrLen) {
                answer += " ";
                loopCnt++;
            }
        }
        
        return answer;
    }
}
