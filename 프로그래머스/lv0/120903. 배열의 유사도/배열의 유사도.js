function solution(s1, s2) {    
    var count = 0
    var answer = s2.map((i) => {
        for (let j of s1) {
            if (i == j) {
                count += 1
            }
        }
    });
    
    return count;
}