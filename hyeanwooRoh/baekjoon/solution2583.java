// 영역 구하기

// 35분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(sb.toString());
	}

  static int N, M, K;
  static int[][] graphPaper;
  static StringBuilder sb;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    graphPaper = new int[N][M];
    for (int i = 0; i < K; i++) {
      st = new StringTokenizer(br.readLine());
      int x1 = Integer.parseInt(st.nextToken());
      int y1 = Integer.parseInt(st.nextToken());
      int x2 = Integer.parseInt(st.nextToken());
      int y2 = Integer.parseInt(st.nextToken());
      paintPaper(y1, x1, y2 - 1, x2 - 1);
    }

    br.close();
  }

  private static void paintPaper(int r1, int c1, int r2, int c2) {
    for (int i = r1; i <= r2; i++) {
      for (int j = c1; j <= c2; j++) {
        graphPaper[i][j] = 1;
      }
    }
  }

	private static void solve() {
    boolean[][] visit = new boolean[N][M];
    ArrayList<Integer> list = new ArrayList<>();

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (graphPaper[i][j] == 0 && !visit[i][j]) {
          list.add(bfs(visit, i,j));
        }
      }
    }

    Collections.sort(list);
    sb = new StringBuilder().append(list.size()).append("\n");
    for(Integer num : list) {
      sb.append(num).append(" ");
    }
	}

  static int[] di = {1,-1,0,0};
  static int[] dj = {0,0,1,-1};
  
  private static int bfs(boolean[][] visit, int r, int c) {
    int cnt = 1;
    Queue<Node> q = new LinkedList<>();
    q.add(new Node(r,c));
    visit[r][c] = true;

    while (!q.isEmpty()) {
      Node tNode = q.poll();

      for (int d = 0; d < 4; d++) {
        int ti = tNode.r + di[d];
        int tj = tNode.c + dj[d];

        if (ti < 0 || ti >= N || tj < 0 || tj >= M) continue;

        if (graphPaper[ti][tj] == 0 && !visit[ti][tj]) {
          q.add(new Node(ti,tj));
          visit[ti][tj] = true;
          cnt++;
        }
      }
    }

    return cnt;
  }

  private static class Node {
    int r;
    int c;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
}
