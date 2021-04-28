// 00:20 ~ 00:48

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    int[] balloons = {-16,27,65,-2,58,-92,-71,-68,-61,-33};
    System.out.println(solution(balloons));
	}

  public static int solution(int[] balloons) {
    int answer = 0;

    int[][] side = new int[balloons.length][2];
    int min = balloons[0];
    for (int i = 1; i < balloons.length - 1; i++) {
      min = Math.min(min, balloons[i]);
      side[i][0] = min;
    }
    
    min = balloons[balloons.length-1];
    for (int i = balloons.length - 2; i > 0; i--) {
      min = Math.min(min, balloons[i]);
      side[i][1] = min;
    }

    int biggerCnt;
    for (int i = 0; i < side.length; i++) {
      if (i == 0 || i == side.length - 1) {
        answer++;
        continue;
      }

      biggerCnt = 0;
      if (balloons[i] > side[i][0]) biggerCnt++;
      if (balloons[i] > side[i][1]) biggerCnt++;
      if (biggerCnt < 2) answer++;
    }

    return answer;
  }
}
