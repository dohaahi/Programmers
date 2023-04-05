function solution(n) {
        let m =1

    for (let i = 1; i <= n; i++) {
        m *= i
        if(m > n) {
            return i - 1
        } if (m == n) {
            return i
        }
    }
}