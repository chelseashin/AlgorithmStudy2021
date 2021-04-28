// 00:00 ~ 00:02

import java.util.*;

public class Main {
	public static void main(String[] args) {
    int[] balloons = {-16,27,65,-2,58,-92,-71,-68,-61,-33};
    System.out.println(solution(balloons));
	}

  public static int solution(int[] absolutes, boolean[] signs) {
    int answer = 0;

    for (int i = 0; i < signs.length; i++) {
      if (signs[i]) {
        answer += absolutes[i];
      } else {
        answer -= absolutes[i];
      }
    }
    return answer;
  }
}
