// 상범 빌딩
// 40분

// 3중 배열 bfs

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    System.out.println(sb.toString());
	}

  static Node start, end;
  static int[][][] building;
  static boolean[][][] visited;
  static StringBuilder sb;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    sb = new StringBuilder();

    while (true) {
      st = new StringTokenizer(br.readLine());
      int L = Integer.parseInt(st.nextToken());
      int R = Integer.parseInt(st.nextToken());
      int C = Integer.parseInt(st.nextToken());

      if (L == 0 && R == 0 && C == 0) break;

      building = new int[L][R][C];
      visited = new boolean[L][R][C];
      for (int i = 0; i < L; i++) {
        for (int j = 0; j < R; j++) {
          char[] input = br.readLine().toCharArray();
          for (int k = 0; k < C; k++) {
            switch (input[k]) {
              case 'S':
                start = new Node(i, j, k, 0);
                break;
              case 'E':
                end = new Node(i, j, k, 0);
                break;
              case '#':
                building[i][j][k] = 1;
                break;
              case '.':
                building[i][j][k] = 0;
                break;
            }
          }
        }
        br.readLine();
      }

      solve(L, R, C);
    }

    br.close();
  }

  static int[] df = {-1, 1, 0, 0, 0, 0};
  static int[] dr = {0, 0, -1, 1, 0, 0};
  static int[] dc = {0, 0, 0, 0, 1, -1};

  private static void solve(int Floor, int Row, int Col) {
    Queue<Node> queue = new LinkedList<>();
    queue.add(start);
    visited[start.f][start.r][start.c] = true;

    while (!queue.isEmpty()) {
      Node tnode = queue.poll();
      int f = tnode.f;
      int r = tnode.r;
      int c = tnode.c;
      int time = tnode.time;

      if (end.f == f && end.r == r && end.c == c) {
        sb.append(ecapedString(time));
        return;
      }

      for (int d = 0; d < 6; d++) {
        int nf = f + df[d];
        int nr = r + dr[d];
        int nc = c + dc[d];

        if (nf < 0 || nf >= Floor || nr < 0 || nr >= Row || nc < 0 || nc >= Col) continue;

        if (building[nf][nr][nc] == 0 && !visited[nf][nr][nc]) {
          queue.add(new Node(nf, nr, nc, time + 1));
          visited[nf][nr][nc] = true;
        }
      }
    }

    sb.append("Trapped!\n");
  }

  private static String ecapedString(int x) {
    return String.format("Escaped in %d minute(s).\n", x);
  }

  static class Node {
    int f;
    int r;
    int c;
    int time;

    public Node(int f, int r, int c, int t) {
      this.f = f;
      this.r = r;
      this.c = c;
      this.time = t;
    }

    @Override
    public String toString() {
      return "("+this.f+","+this.r+","+this.c+" "+this.time+")";
    }
  }

}
