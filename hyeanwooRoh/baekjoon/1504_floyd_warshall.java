// 특정한 최단 경로
// 55분

// 플로이드-와샬 알고리즘
// 1636ms

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N, v1, v2;
  static long[][] graph;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    int E = Integer.parseInt(st.nextToken());

    graph = new long[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (i != j) graph[i][j] = Integer.MAX_VALUE;
      }
    }

    for (int i = 0; i < E; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;
      int c = Integer.parseInt(st.nextToken());

      graph[a][b] = c;
      graph[b][a] = c;
    }

    st = new StringTokenizer(br.readLine());
    v1 = Integer.parseInt(st.nextToken()) - 1;
    v2 = Integer.parseInt(st.nextToken()) - 1;

    br.close();
  }

  public static void solve() {
    for (int k = 0; k < N; k++) {
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          if (i == j) continue;
          graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
        }
      }
    }

    long answer = Math.min(graph[0][v1] + graph[v1][v2] + graph[v2][N-1], graph[0][v2] + graph[v2][v1] + graph[v1][N-1]);
    if (answer >= Integer.MAX_VALUE) {
      System.out.println(-1);
    } else {
      System.out.println(answer);
    }
  }
}