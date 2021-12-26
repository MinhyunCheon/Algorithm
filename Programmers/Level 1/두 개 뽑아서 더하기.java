문제 설명
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.



import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        int len = numbers.length;
        Set<Integer> set = new HashSet<Integer>();
        int idx = 0;
        
        for(int x = 0; x < len; x++) {
            for(int y = x + 1; y < len; y++) {
                set.add(numbers[x] + numbers[y]);
            }
        }
        
        answer = new int[set.size()];
        Iterator it = set.iterator();
        while(it.hasNext()) {
            answer[idx] = (int)it.next();
            idx++;
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}
