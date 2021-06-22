// 별 찍기 - 10
// 43분

import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
    solve();
	}

  public static void solve() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    br.close();

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        dfs(sb, N, i, j);
      }
      sb.append("\n");
    }

    System.out.println(sb.toString());
  }


  static void dfs(StringBuilder sb, int n, int i, int j) {
    if ((i / n) % 3 == 1 && (j / n) % 3 == 1) {
      sb.append(" ");
    } else {
      if (n / 3 == 0) {
        sb.append("*");
      } else {
        dfs(sb, n/3, i, j);
      }
    }
  }
}