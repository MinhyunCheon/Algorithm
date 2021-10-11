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



function solution(answers) {
    var answer = [];
    const u1 = [1,2,3,4,5];
    const u2 = [2,1,2,3,2,4,2,5];
    const u3 = [3,3,1,1,2,2,4,4,5,5];
    const u1Max = u1.length;
    const u2Max = u2.length;
    const u3Max = u3.length;
    const map = new Map();
    
    let u1Index = 0;
    let u2Index = 0;
    let u3Index = 0;
    
    // console.log(answers);
    answers.forEach(n => {
        // console.log(u3Max);
        if(n == u1[u1Index]) map.set(1, map.has(1) ? map.get(1) + 1 : 1);
        if(++u1Index >= u1Max) u1Index = 0;
        
        if(n == u2[u2Index]) map.set(2, map.has(2) ? map.get(2) + 1 : 1);
        if(++u2Index >= u2Max) u2Index = 0;
        
        if(n == u3[u3Index]) map.set(3, map.has(3) ? map.get(3) + 1 : 1);
        if(++u3Index >= u3Max) u3Index = 0;
    });
    
    // console.log(map.get(1));
    const it = map.entries();
    let arr2 = [];
    let index = 0;
    let maxScore = 0;
    for(let i of it) {
        // console.log(i);
        arr2[index++] = i;
        // console.log(i[1]);
        if(maxScore < i[1]) maxScore = i[1];
    }
    
    let answerIndex = 0;
    arr2.forEach(e => {
        // console.log(e);
        if(e[1] == maxScore) {
            answer[answerIndex++] = e[0];
        }
    });
    // console.log(answer);
    answer.sort();
    
    return answer;
}
