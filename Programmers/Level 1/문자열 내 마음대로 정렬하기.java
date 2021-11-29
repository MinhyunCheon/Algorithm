문제 설명
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

제한 조건
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.



import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        ArrayList<String> arrayList = new ArrayList<>();
        
        for(String s : strings) arrayList.add(s);
        
        arrayList.sort((s1, s2) -> {
            char s1Char = s1.charAt(n);
            char s2Char = s2.charAt(n);
            int sLen = s1.length();
            
            if(s1Char != s2Char) return s1Char - s2Char;

            for(int idx = 0; idx < sLen; idx++) {
                if(s1.charAt(idx) == s2.charAt(idx)) continue;
                else return s1.charAt(idx) - s2.charAt(idx);
            }
            
            return 0;   // 해당 라인을 선언하지 않으면 런타임 에러 발생
        });
        
        answer = arrayList.toArray(new String[0]);
            
        return answer;
    }
}
