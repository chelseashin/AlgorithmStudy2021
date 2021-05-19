// 두 용액
// 1시간 4분

// 알고리즘 분류에 이진탐색이 있어서 적용하느라 시간을 날렸다
// 그냥 두 포인터만 써서 해결

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(answer[0] + " " + answer[1]);
	}

  static int[] liquid, answer;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    
    liquid = new int[n];
    answer = new int[2];
    answer[1] = Integer.MAX_VALUE;

    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      liquid[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(liquid);

    br.close();
  }

  public static void solve() {
    int left = 0;
    int right = liquid.length - 1;
    int max = Integer.MAX_VALUE;

    while (left < right) {
      int sum = liquid[left] + liquid[right];

      if (Math.abs(sum) < max) {
        answer[0] = liquid[left];
        answer[1] = liquid[right];
        max = Math.abs(sum);
      }

      if (sum > 0) {
        right--;
      } else {
        left++;
      }
    }
  }
}
