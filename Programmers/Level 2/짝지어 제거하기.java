문제 설명
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.
그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.



import java.util.Stack;

class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        Stack<Character> stack = new Stack();
        // String[] sArr = s.split("");
        // stack.push(sArr[0]);
        int sLen = s.length();
        
        for(int idx = 0; idx < sLen; idx++) {
            if(!stack.empty() && stack.peek() == s.charAt(idx)) stack.push(s.charAt(idx));
            else stack.push(s.charAt(idx));
        }
        
        // 효율성 2번 통과/실패 번갈아 출력
        // for(String ss : sArr) {
        //     if(!stack.empty() && stack.peek().equals(ss)) stack.pop();
        //     else stack.push(ss);
        // }
        
        // 위 코드보다 메모리 소모량 증가
        // for(int idx = 1; idx < sArrLen; idx++) {
        //      if(!stack.empty() && stack.peek().equals(sArr[idx])) stack.pop();
        //      else stack.push(sArr[idx]);
        // }
        
        if(stack.empty()) answer = 1;
        
        return answer;
    }
}
