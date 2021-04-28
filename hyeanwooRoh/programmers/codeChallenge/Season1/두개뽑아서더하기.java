// 00:00 ~ 00:20

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    int[] numbers = {2,1,3,4,1};
    int[] result = solution(numbers);
    System.out.println(Arrays.toString(result));
	}

  public static int[] solution(int[] numbers) {
    boolean[] sumNums = new boolean[401];
    for (int i = 0; i < numbers.length; i++) {
      for (int j = i + 1; j < numbers.length; j++) {
        sumNums[numbers[i]+numbers[j]] = true;
      }
    }

    int len = 0;
    for (int i = 0; i < sumNums.length; i++) {
      if (sumNums[i]) len++;
    }

    int[] answer = new int[len];
    int idx = 0;
    for (int i = 0; i < sumNums.length; i++) {
      if (sumNums[i]) answer[idx++] = i;
    }

    return answer;
  }
}