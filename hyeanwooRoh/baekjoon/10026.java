// 적록색약
// 38분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static final int R = 17, G = 6, B = 1;
  static int N;
  static int[][] colors;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    N = Integer.parseInt(br.readLine());
    colors = new int[N][N];

    for (int i = 0; i < N; i++) {
      char[] tmp = br.readLine().toCharArray();
      for (int j = 0; j < N; j++) {
        colors[i][j] = tmp[j] - 'A';
      }
    }

    br.close();
  }

  public static void solve() {
    StringBuilder sb = new StringBuilder();
    boolean[][] visited;
    int area = 0;

    visited = new boolean[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (!visited[i][j]) {
          bfs(i, j, visited);
          area++;
        }
      }
    }
    sb.append(area).append(" ");
    
    area = 0;
    visited = new boolean[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (!visited[i][j]) {
          bfsColorBlind(i, j, visited);
          area++;
        }
      }
    }
    sb.append(area);

    System.out.println(sb.toString());
  }

  static int[] di = {0,0,1,-1};
  static int[] dj = {1,-1,0,0};

  static void bfs(int sr, int sc, boolean[][] visited) {
    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(sr, sc));
    visited[sr][sc] = true;

    int stColor = colors[sr][sc];
    while (!queue.isEmpty()) {
      Node node = queue.poll();

      for (int d = 0; d < 4; d++) {
        int nr = node.r + di[d];
        int nc = node.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc]) continue;

        if (colors[nr][nc] == stColor) {
          queue.add(new Node(nr, nc));
          visited[nr][nc] = true;
        }
      }
    }
  }

  
  static void bfsColorBlind(int sr, int sc, boolean[][] visited) {
    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(sr, sc));
    visited[sr][sc] = true;

    int stColor = colors[sr][sc];
    while (!queue.isEmpty()) {
      Node node = queue.poll();

      for (int d = 0; d < 4; d++) {
        int nr = node.r + di[d];
        int nc = node.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc]) continue;

        if (colors[nr][nc] == stColor) {
          queue.add(new Node(nr, nc));
          visited[nr][nc] = true;
        } else if ((stColor == R || stColor == G) && (colors[nr][nc] == R || colors[nr][nc] == G)) {
          queue.add(new Node(nr, nc));
          visited[nr][nc] = true;
        }
      }
    }
  }

  static class Node {
    int r; int c;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
}