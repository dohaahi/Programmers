class Solution {
    public int[] solution(int[] num_list) {
        // num_list와 같은 길이인 새로운 배열 만들기
        int[] answer = new int [num_list.length];

        // 새로 만든 배열에 기존 배열 값들을 반대로 삽입
        for(int i=0; i<num_list.length; i++){
            answer[i] = num_list[num_list.length - 1-i];
        }
        
        return answer;
    }
}