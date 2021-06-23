// 인하니카 공화국

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int T = Integer.parseInt(br.readLine());
    for (int tc = 0; tc < T; tc++) {
      init(br);
      dynamite[1][0] = Integer.MAX_VALUE;
      int answer = solve(0,1);
      if (answer == Integer.MAX_VALUE) answer = 0;
      sb.append(answer).append("\n");
    }
    br.close();

    System.out.println(sb.toString());
	}

  static int N, M;
  static int[][] dynamite;

  public static void init(BufferedReader br) throws IOException {
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    dynamite = new int[N+1][N+1];
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      int d = Integer.parseInt(st.nextToken());
      dynamite[a][b] = d;
      dynamite[b][a] = d;
    }
  }

  public static int solve(int par, int cur) {
    int sum = 0;
    for (int i = 1; i <= N; i++) {
      if (dynamite[cur][i] > 0 && i != par) {
        sum += solve(cur, i);
      }
    }

    if (sum == 0) return dynamite[cur][par];
    
    return Math.min(sum, dynamite[cur][par]);
  }
}