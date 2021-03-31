// 포도주 시식
// 1시간 23분

// 50분 동안 아무리 고민해도 풀이가 떠오르지않아서 답을 보고 해결했다
// dp는 사실상 점화식풀이라고 봐도 무방하다
// 다음부터는 주어진 조건을 활용해 점화식을 만들어보는 식으로 접근하자

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N;
  static int[] wines;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    wines = new int[N];

    for (int i = 0; i < N; i++) {
      wines[i] = Integer.parseInt(br.readLine());
    }
    br.close();
  }

  private static void solve() {
    if (N == 1) {
      System.out.println(wines[0]);
      return ;
    } else if (N == 2) {
      System.out.println(wines[0] + wines[1]);
      return ;
    }

    int[] dp = new int[N];

    dp[0] = wines[0];
    dp[1] = wines[0] + wines[1];
    dp[2] = Math.max(dp[1], Math.max(dp[0], wines[1]) + wines[2]);

    for (int i = 3; i < N; i++) {
      dp[i] = Math.max(dp[i-1], Math.max(dp[i-2], dp[i-3] + wines[i-1]) + wines[i]);
    }

    System.out.println(dp[N-1]);
  }
}
