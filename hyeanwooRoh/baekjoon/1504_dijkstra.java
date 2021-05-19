// 특정한 최단 경로
// 55분

// 다익스트라
// 468ms

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N, p1, p2;
  static int[][] graph;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    int E = Integer.parseInt(st.nextToken());

    graph = new int[N][N];
    for (int i = 0; i < E; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;
      int c = Integer.parseInt(st.nextToken());

      graph[a][b] = c;
      graph[b][a] = c;
    }

    st = new StringTokenizer(br.readLine());
    p1 = Integer.parseInt(st.nextToken()) - 1;
    p2 = Integer.parseInt(st.nextToken()) - 1;

    br.close();
  }

  public static void solve() {
    int dist1 = dijkstra(0, p1) + dijkstra(p1, p2) + dijkstra(p2, N - 1);
    int dist2 = dijkstra(0, p2) + dijkstra(p2, p1) + dijkstra(p1, N - 1);

    int answer = Math.min(dist1, dist2);
    if (answer >= 10000000) {
      System.out.println(-1);
    } else {
      System.out.println(answer);
    }
  }

  static int dijkstra(int v1, int v2) {
    boolean[] visited = new boolean[N];
    int[] dist = new int[N];
    Arrays.fill(dist, 10000000);
    
    dist[v1] = 0;

    for (int i = 0; i < N; i++) {
      int min = Integer.MAX_VALUE;
      int cur = 0;

      for (int j = 0; j < N; j++) {
        if (!visited[j] && min > dist[j]) {
          min = dist[j];
          cur = j;
        }
      }

      visited[cur] = true;
      if (cur == v2) break;

      for (int j = 0; j < N; j++) {
        if (!visited[j] && graph[cur][j] != 0 && dist[j] > min + graph[cur][j]) {
          dist[j] = min + graph[cur][j];
        }
      }
    }

    return dist[v2];
  }

}