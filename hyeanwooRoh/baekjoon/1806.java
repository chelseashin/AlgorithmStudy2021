// 부분합
// 33분

// 경우의 수가 없을 때 처리를 빼먹은 부분 빼고는 수월했다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N, S;
  static int[] numbers;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    S = Integer.parseInt(st.nextToken());

    numbers = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      numbers[i] = Integer.parseInt(st.nextToken());
    }
    br.close();
  }

  public static void solve() {
    int l = 0;
    int r = 1;
    int len = Integer.MAX_VALUE;
    int sum = numbers[0];

    while (r < numbers.length) {
      sum += numbers[r];

      if (sum > S) {
        while (sum - numbers[l] >= S) {
          sum -= numbers[l];
          l++;
        }
        len = Math.min(len, r - l + 1);
      } else if (sum == S) {
        len = Math.min(len, r - l + 1);
      }

      r++;
    }

    if (len == Integer.MAX_VALUE) {
      System.out.println(0);
    } else {
      System.out.println(len);
    }
  }
}