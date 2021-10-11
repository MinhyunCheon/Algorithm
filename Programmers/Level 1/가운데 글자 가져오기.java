문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
  
  
  
class Solution {
  public String solution(String s) {
      String answer = "";
      int len = s.length();
      int startIndex = (len / 2);
      
      if(len % 2 == 1) {
          answer = s.substring(startIndex, startIndex + 1);
      }
      else {
          answer = s.substring(startIndex - 1, startIndex + 1);
      }
      
      return answer;
  }
}
