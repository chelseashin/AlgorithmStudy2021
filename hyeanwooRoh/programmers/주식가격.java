// 53분
// 조건을 잘못이해해서 반례 참고
// 스택을 써볼까했지만 방법이 생각나지않아 완전탐색 사용
// 프로그래머스는 반례가 다양하지않아서 참고용으로만 푸는게 나을듯

class Solution {
  public static int[] solution(int[] prices) {
    int[] answer = new int[prices.length];

    int idx = 0;
    int cnt = 0;
    for (int i = 0; i < answer.length - 1; i++) {
      int num1 = prices[i];
      for (int j = i+1; j < answer.length; j++) {
        int num2 = prices[j];
        cnt++;
        if(num1 > num2) {
          break;
        }
      }
      answer[idx++] = cnt;
      cnt = 0;
    }

    return answer;
  }
}