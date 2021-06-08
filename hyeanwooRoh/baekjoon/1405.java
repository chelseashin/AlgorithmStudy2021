// 미친 로봇
// 40분

// 백트래킹하면서 더해주기

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    backtracking(0, N, N, 1);
    System.out.println(String.format("%.10f", answer));
	}

  static int N;
  static boolean[][] visited;
  static double answer = 0;
  static double[] percent = new double[4];

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    visited = new boolean[2*N+1][2*N+1];
    visited[N][N] = true;

    for (int i = 0; i < 4; i++) {
      percent[i] = Double.parseDouble(st.nextToken()) / 100;
    }
    br.close();
  }

  static int[] di = {0,0,1,-1};
  static int[] dj = {1,-1,0,0};

  public static void backtracking(int depth, int r, int c, double p) {
    if (depth == N) {
      answer += p;
      return;
    }

    for (int d = 0; d < 4; d++) {
      int nr = r + di[d];
      int nc = c + dj[d];

      if (nr < 0 || nr >= visited.length || nc < 0 || nc >= visited[0].length || visited[nr][nc]) continue;

      visited[nr][nc] = true;
      backtracking(depth+1, nr, nc, p * percent[d]);
      visited[nr][nc] = false;
    }
  }
}